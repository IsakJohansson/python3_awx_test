#!/usr/bin/python3

import sys
from ansible.module_utils.basic import *

def send_request():
    version = sys.version

    module = AnsibleModule(argument_spec={})
    module.exit_json(changed=True, version=version)


send_request()
