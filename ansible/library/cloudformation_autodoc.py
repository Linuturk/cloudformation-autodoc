#!/usr/bin/python

DOCUMENTATION = '''
---
module: cloudformation_autodoc
author: "Justin Phelps"
version_added: "0.1"
short_description: Document Cloud Formation Templates
requirements: cfautodoc
description:
    - Automatically generate a README.md file from a Cloud Formation template.
options:
    template:
        required: true
        aliases: [ "name" ]
        description:
            - Path to the Cloud Formation Template to document.
    dest:
        required: false
        description:
            - Set the path to the markdown file.
        default: "README.md"
    timestamp:
        required: false
        description:
            - Append a timestamp to the end of the documentation.
        choices: [ "yes", "no" ]
        default: "no"
    insert:
        required: false
        description:
            - Insert a markdown file into the generated documentation.
'''

EXAMPLES = '''
# Document the Cloud Formation Template BasicNetwork.template
- cloudformation_autodoc: template=BaseNetwork.template

# Override the markdown file name
- cloudformation_autodoc: template=MyTemplate.template dest=OTHER.md

# Append a timestamp to the outputted documentation
- cloudformation_autodoc: template=MyTemplate.template timestamp=yes

# Insert the specified file into the final document
- cloudformation_autodoc: template=MyTemplate.template insert=insert.md
'''

from ansible.module_utils.basic import *  # noqa
from ansible.utils.hashing import secure_hash, secure_hash_s


def main():

    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(default='README.md'),
            template=dict(required=True),
            name=dict(aliases=['template']),
            timestamp=dict(default='no', choices=['yes', 'no']),
            insert=dict(default=False)
        ),
        supports_check_mode=False
    )

    # Try to import the library
    try:
        from cfautodoc.autodoc import autodoc
    except ImportError:
        module.fail_json(msg='Install the cfautodoc tool using pip.')

    templ = module.params['name']
    dest = module.params['dest']
    timestamp = module.params['timestamp']
    insert = module.params['insert']

    # Massage timestamp for library
    if timestamp == 'yes':
        timestamp = True
    else:
        timestamp = False

    # Generate the Markdown
    towrite = autodoc(templ, dest, timestamp, insert)

    # Write the towrite list
    if secure_hash(dest) == secure_hash_s(''.join(towrite)):
        msg = 'Documentation already up to date for {0}'.format(templ)
        module.exit_json(changed=False, written=msg)
    else:
        try:
            with open(dest, 'w') as destination:
                for line in towrite:
                    destination.write(line)
            msg = '{0} documentation updated to {1}'.format(templ, dest)
            module.exit_json(changed=True, written=msg)
        except Exception as exc:
            module.fail_json(msg=exc)


if __name__ == '__main__':
    main()
