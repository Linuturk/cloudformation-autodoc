#!/usr/bin/python

import datetime
import json


def heading(string, level=2):
    '''
    Takes a string and wraps it with a heading.
    '''
    return '\n{0} {1}\n'.format('#' * level, string)


def autodoc(template, documentation, timestamp=False, insert=False):

    # Open the template file
    try:
        with open(template) as t:
            data = json.load(t)
    except Exception as exc:
        raise(exc)

    towrite = []
    # Write out the Description
    if 'Description' in data:
        towrite.append(heading('Description'))
        towrite.append(data['Description'])

    # Insert the insert
    if insert:
        try:
            with open(insert) as insertf:
                for line in insertf:
                    towrite.append(line)
        except Exception as exc:
            raise(exc)

    # Metadata section
    if 'Metadata' in data:
        towrite.append(heading('Metadata', level=4))
        for key, value in sorted(data['Metadata'].iteritems()):
            towrite.append(' * **{0}**: {1}'.format(key, value))

    # Generate the Parameters
    if 'Parameters' in data:
        towrite.append(heading('Parameters'))
        for key, value in sorted(data['Parameters'].iteritems()):
            towrite.append(' * **{0}** - {1}'.format(key,
                           value['Description']))
            if 'Default' in value:
                towrite.append('  * Default: `{0}`'.format(value['Default']))
            if 'ConstraintDescription' in value:
                towrite.append('  * Constraint: `{0}`'.format(
                               value['ConstraintDescription']))

    # Generate any Conditions if they exist
    if 'Conditions' in data:
        towrite.append(heading('Conditions'))
        for key, value in sorted(data['Conditions'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value))

    # Generate any Mappings if they exist
    if 'Mappings' in data:
        towrite.append(heading('Mappings'))
        for key, value in sorted(data['Mappings'].iteritems()):
            towrite.append(' * **{0}**:'.format(key))
            for key in value.iteritems():
                towrite.append('  * `{0}`'.format(key))

    # Generate a list of all Resources
    if 'Resources' in data:
        towrite.append(heading('Resources'))
        for key, value in sorted(data['Resources'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value['Type']))

    # Generate the Outputs
    if 'Outputs' in data:
        towrite.append(heading('Outputs'))
        for key, value in sorted(data['Outputs'].iteritems()):
            towrite.append(' * **{0}** - `{1}`'.format(key, value['Value']))

    # Show when the file was last updated
    if timestamp:
        time = str(datetime.datetime.now())
        towrite.append('\n**Last Updated:** {0}'.format(time))

    return "\n".join(towrite)


if __name__ == '__main__':
    pass
