#!/usr/bin/python

DOCUMENTATION = '''
---
module: cloudformation_autodoc
author: "Justin Phelps"
version_added: "0.1"
short_description: Document Cloud Formation Templates
requirements: None
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
            - Set the path to the markdown file. (Default: README.md)
'''

EXAMPLES = '''
# Document the Cloud Formation Template BasicNetwork.template
- cloudformation_autodoc: template=BaseNetwork.template

# Override the markdown file name
- cloudformation_autodoc: template=MyTemplate.template dest=OTHER.md
'''

import datetime
import json


def main():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(default='README.md'),
            template=dict(required=True),
            name=dict(aliases=['template'])
        ),
        supports_check_mode=False
    )

    templ = module.params['name']
    dest = module.params['dest']

    # Open the template file
    try:
        with open(templ) as template:
            data = json.load(template)
    except Exception as exc:
        module.fail_json(msg=exc)

    towrite = []
    # Write out the Description
    if 'Description' in data:
        towrite.append('##{0}'.format('Description'))
        towrite.append(data['Description'])

    # Metadata section
    if 'Metadata' in data:
        towrite.append('####{0}'.format('Metadata'))
        for key, value in sorted(data['Metadata'].iteritems()):
            towrite.append(' * **{0}**: {1}'.format(key, value))
        towrite.append('\n')

    # Generate the Parameters
    if 'Parameters' in data:
        towrite.append('##{0}'.format('Parameters'))
        for key, value in sorted(data['Parameters'].iteritems()):
            towrite.append(' * **{0}** - {1}'.format(key,
                           value['Description']))
            if 'Default' in value:
                towrite.append('  * Default: `{0}`'.format(value['Default']))
            if 'ConstraintDescription' in value:
                towrite.append('  * Constraint: `{0}`'.format(
                               value['ConstraintDescription']))
    towrite.append('\n')

    # Generate any Conditions if they exist
    if 'Conditions' in data:
        towrite.append('##{0}'.format('Conditions'))
        for key, value in sorted(data['Conditions'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value))
        towrite.append('\n')

    # Generate any Mappings if they exist
    if 'Mappings' in data:
        towrite.append('##{0}'.format('Mappings'))
        for key, value in sorted(data['Mappings'].iteritems()):
            towrite.append(' * **{0}**:'.format(key))
            for key in value.iteritems():
                towrite.append('  * `{0}`'.format(key))
        towrite.append('\n')

    # Generate a list of all Resources
    if 'Resources' in data:
        towrite.append('##{0}'.format('Resources'))
        for key, value in sorted(data['Resources'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value['Type']))
        towrite.append('\n')

    # Generate the Outputs
    if 'Outputs' in data:
        towrite.append('##{0}'.format('Outputs'))
        for key, value in sorted(data['Outputs'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value['Value']))
        towrite.append('\n')

    # Show when the file was last updated
    time = str(datetime.datetime.now())
    towrite.append('**Last Updated:** {0}'.format(time))

    # Write the towrite list
    try:
        with open(dest, 'w') as destination:
            for line in towrite:
                destination.write('{0}\n'.format(line))
        msg = '{0} documentation updated to {1}'.format(templ, dest)
        module.exit_json(changed=True, written=msg)
    except Exception as exc:
        module.fail_json(msg=exc)


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
