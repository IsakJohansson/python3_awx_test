#!/usr/bin/python3

import sys
from ansible.module_utils.basic import *

def send_request():
    version = sys.version
    py_path = sys.path
    module = AnsibleModule(argument_spec={})
    module.exit_json(changed=True, path=py_path, version=version)


send_request()
