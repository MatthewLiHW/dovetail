#!/usr/bin/env python
#
# grakiss.wanglei@huawei.com
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#


import click
import yaml
import os

import utils.dovetail_logger as dt_logger
import utils.dovetail_utils as dt_utils

from container import Container 
from conf.dovetail_config import *

logger = dt_logger.Logger('run.py').getLogger()


def load_certification():
    with open(CERT_PATH) as f:
        cert_yaml = yaml.safe_load(f)
    logger.debug(cert_yaml)
    return cert_yaml

def load_scenario(scenario):
    scenario_list = {}
    for root, dirs, files in os.walk(CERT_PATH):
        for scenario_yaml in files:
            with open(os.path.join(root, scenario_yaml)) as f: 
                scenario_yaml = yaml.safe_load(f)
                scenario_list.update(scenario_yaml)
            
    logger.debug(scenario_list)
    return scenario_list[SCENARIO_NAMING_FMT % scenario]

def load_testcase():
    testcase_list = {}
    for root, dirs, files in os.walk(TESTCASE_PATH):
        for testcase_file in files:
            with open(os.path.join(root, testcase_file)) as f:
                testcase_yaml = yaml.safe_load(f)
                testcase_list.update(testcase_yaml)
    logger.debug( testcase_list )
    return testcase_list

def get_container():
    return None


def get_result():
    return None

def run_test(scenario, testcases):
    result_list = []
    for testcase in scenario['testcase_list']:
        logger.info('>>[testcase]: %s' % (testcase))
        Container.pull_image(testcases[testcase]['scripts']['type'])
        container_id = get_container()
        if not container_id:
            container_id = Container.create(testcases[testcase]['scripts']['type'])
        logger.debug('container id:%s' % container_id)
        
        result = get_result()
        if not result:

            #sub_cmd = ' echo test  > /home/opnfv/functest/results/functest_dovetail.log'
            sub_cmd = 'python /home/opnfv/repos/functest/ci/prepare_env.py start'
            cmd = 'sudo docker exec %s %s' % (container_id, sub_cmd) 
            dt_utils.exec_cmd(cmd,logger,exit_on_error=False)
            sub_cmd = 'python /home/opnfv/repos/functest/ci/run_tests.py -t %s -r' % testcases[testcase]['scripts']['testcase']
            cmd = 'sudo docker exec %s %s' % (container_id, sub_cmd)
            dt_utils.exec_cmd(cmd,logger, exit_on_error = False)
            result = get_results_from_db(testcases[testcase]['scripts']['testcase'])

        if result is not None:
            logger.debug(result)          
            result_list.append(result)
    return result_list

import json
import urllib2

def get_results_from_db(testcase):
    #url = ft_utils.get_db_url() + '/results?build_tag=' + BUILD_TAG
    url = 'http://testresults.opnfv.org/test/api/v1/results?case=%s&last=1' % testcase
    logger.debug("Query to rest api: %s" % url)
    try:
        data = json.load(urllib2.urlopen(url))
        return data['results'][0]
    except:
        logger.error("Cannot read content from the url: %s" % url)
        return None

def generate_report(result_list, scenario_yaml, testcases):
    report = ''

    logger.info('')
    logger.info('****************************************')
    logger.info('                report                  ') 
    logger.info('****************************************')
    logger.info('scenario: %s' % scenario_yaml['name'])
    for testcase_name in scenario_yaml['testcase_list']:
        testcase = testcases[testcase_name]
        logger.info('   testcase: %s' % testcase_name)
        logger.info('   desc: %s' % testcase['description'])
        if testcase['scripts']['sub_testcase_list'] is not None:
            for subtest in testcase['scripts']['sub_testcase_list']:
                logger.info('       %s' % subtest)

    for result in result_list:
        formal_result = '[testcase]: %s [%s]' % (result['case_name'],result['criteria'])
        logger.info(formal_result)
        report += formal_result

    return report

@click.command()
@click.option('--scenario', default='basic', help='certification scenario')
def main(scenario):
    """Dovetail certification test entry!"""
    logger.info('=======================================')
    logger.info('Dovetail certification: %s!' % scenario)
    logger.info('=======================================')
    #cert = load_certification()
    testcases = load_testcase()
    scenario_yaml = load_scenario(scenario)
    result_list = run_test(scenario_yaml,testcases)
    generate_report(result_list, scenario_yaml, testcases)

if __name__ == '__main__':
    main()
