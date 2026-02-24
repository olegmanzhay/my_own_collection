#!/usr/bin/python

# Copyright: (c) 2024, Your Name <your.email@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Create a text file with specified content on a remote host
version_added: "1.0.0"
description:
    - Creates a text file at the specified path with the given content.
    - Is idempotent: won't recreate the file if it already exists with the same content.
options:
    path:
        description: Path where the file should be created.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: true
        type: str
author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with custom content
  my_own_module:
    path: /tmp/test_file.txt
    content: "Hello, this is a test file!"
'''

RETURN = r'''
result:
    description: Message about the operation result.
    type: str
    returned: always
    sample: "File created successfully"
changed:
    description: Whether the file was created or updated.
    type: bool
    returned: always
    sample: true
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    # Define module arguments
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # Initialize result dictionary
    result = dict(
        changed=False,
        result=''
    )

    # Create AnsibleModule instance
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Extract parameters
    file_path = module.params['path']
    file_content = module.params['content']

    # Check if file exists and get its current content
    file_exists = os.path.exists(file_path)
    current_content = ''
    if file_exists:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except Exception as e:
            module.fail_json(msg=f"Failed to read existing file: {str(e)}", **result)

    # Determine if changes are needed
    needs_update = not file_exists or current_content != file_content

    # Handle check mode
    if module.check_mode:
        result['changed'] = needs_update
        if needs_update:
            result['result'] = "File would be created/updated"
        else:
            result['result'] = "File is up to date"
        module.exit_json(**result)

    # Perform the actual operation if changes are needed
    if needs_update:
        try:
            # Create or update the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            result['changed'] = True
            if file_exists:
                result['result'] = "File content updated"
            else:
                result['result'] = "File created successfully"
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {str(e)}", **result)
    else:
        result['result'] = "File already exists with correct content"

    # Return results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
