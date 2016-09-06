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

logger = dt_logger.Logger('downloader.py').getLogger()

from conf.functest_config import *

class Downloader:

    @classmethod    
    def download_upstream(image):
        cmd = 'sudo docker pull '+ image 
        dt_utils.exec_cmd(cmd,logger)
        #dt_utils.exec_cmd('echo download_upstream',logger)

