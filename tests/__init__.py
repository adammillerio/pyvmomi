# VMware vSphere Python SDK tests
#
# Copyright (c) 2008-2025 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import unittest

from vcr import config
from vcr.stubs import VCRHTTPConnection, VCRHTTPSConnection

from pyVmomi import SoapAdapter
from pyVim import connect


def tests_resource_path(local_path=''):
    this_file = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_file, local_path)

# Fully qualified path to the fixtures directory underneath this module
fixtures_path = tests_resource_path('fixtures')

class VCRTestBase(unittest.TestCase):
    my_vcr = config.VCR(
        custom_patches=(
            (SoapAdapter, 'HTTPConnection', VCRHTTPConnection),
            (SoapAdapter, 'HTTPSConnection', VCRHTTPSConnection),
            (connect, 'HTTPConnection', VCRHTTPConnection),
            (connect, 'HTTPSConnection', VCRHTTPSConnection),
        )
    )

    def setUp(self):
        logging.basicConfig()
        vcr_log = logging.getLogger('vcr')
        vcr_log.setLevel(logging.WARNING)
