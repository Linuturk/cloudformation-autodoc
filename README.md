# cloudformation-autodoc
[![Circle CI](https://circleci.com/gh/Linuturk/cloudformation-autodoc.svg?style=svg)](https://circleci.com/gh/Linuturk/cloudformation-autodoc)

## Install

`pip install cfautodoc`

## Usage

```
usage: cfautodoc [-h] [--output OUTPUT] [--timestamp TIMESTAMP]
                 [--insert INSERT]
                 template

Document CloudFormation templates in Markdown.

positional arguments:
  template              the JSON template to document

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT       Output the Markdown
  --timestamp TIMESTAMP
                        Add a timestamp to the end of the output.
  --insert INSERT       Block of Markdown to insert into the output.
```

## Ansible Module

To install place `ansible/library/cloudformation_autodoc.py` in the [library path](http://docs.ansible.com/ansible/intro_configuration.html#library) for Ansible.
