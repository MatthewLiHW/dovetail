#!/usr/bin/env python
#
# grakiss.wanglei@huawei.com
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#

import utils.dovetail_logger as dt_logger
import utils.dovetail_utils as dt_utils

logger = dt_logger.Logger('container.py').getLogger()

FUNCTEST_DOCKER_IMAGE = 'opnfv/functest:latest'


class Container:

    container_list = {}

    def __init__(cls):
        pass

    def __str__(cls):
        pass

    @classmethod
    def get(cls, type):
        return cls.container_list[type]

    @classmethod
    def create(cls, type):
        #sshkey="-v /root/.ssh/id_rsa:/root/.ssh/id_rsa "
        sshkey = ''
        result_volume = ' -v /home/opnfv/dovetail/results:/home/opnfv/functest/results '
        cmd = 'sudo docker run --privileged=true -id -e INSTALLER_TYPE=compass -e CI_DEBUG=true '+ result_volume + sshkey + FUNCTEST_DOCKER_IMAGE+' /bin/bash'
        dt_utils.exec_cmd(cmd,logger)
        ret, container_id=dt_utils.exec_cmd("sudo docker ps | grep "+FUNCTEST_DOCKER_IMAGE + " | awk '{print $1}' | head -1",logger)
        cls.container_list[type] = container_id
        return container_id

        
        
    
