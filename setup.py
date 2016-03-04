from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(name='cfautodoc',
      version='0.1.3',
      description='Tool to document CloudFormation templates in Markdown.',
      long_description=readme(),
      url='http://github.com/linuturk/cloudformation-autodoc',
      download_url='http://github.com/linuturk/cloudformation-autodoc/tarball/master',  # noqa
      author='Justin Phelps',
      author_email='linuturk@onitato.com',
      license='MIT',
      packages=['cfautodoc'],
      package_data={'cfautodoc': ['README.md']},
      scripts=['bin/cfautodoc'],
      install_requires=[
          'argparse',
      ],
      zip_safe=False)
