#!/usr/bin/env python
#
# grakiss.wanglei@huawei.com
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#

CERT_PATH = './cert/'
TESTCASE_PATH = './testcase/'
SCENARIO_NAMING_FMT = 'certification_%s'

import yaml
import os

with open('conf/functest_config.yml') as f:
    functest_config = yaml.safe_load(f)

container_config = {}

container_config['functest'] = functest_config
