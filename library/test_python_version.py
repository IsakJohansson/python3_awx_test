#!/usr/bin/python3

import sys
from ansible.module_utils.basic import *

def send_request():
    version = sys.version
    fields = {
        "domain_name": {"required": True, "type": "str"},
        }

    module = AnsibleModule(argument_spec=fields)
    domain_name = module.params['domain_name']

    if "www." in domain_name:
        domain_name = domain_name.replace('www.', '')

    domain_name = domain_name.lower()

    domain_name = bytes(domain_name, 'idna')
    # file_name, file_content = namecheap_api.edit_dcv_method()
    module.exit_json(changed=True, version=version, domain_name=domain_name)


send_request()
