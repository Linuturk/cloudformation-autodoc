from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='cfautodoc',
      version='0.1',
      description='Tool to document CloudFormation templates in Markdown.',
      long_description=readme(),
      url='http://github.com/linuturk/cloudformation-autodoc',
      download_url='http://github.com/linuturk/cloudformation-autodoc/tarball/master',  # noqa
      author='Justin Phelps',
      author_email='linuturk@onitato.com',
      license='MIT',
      packages=['cfautodoc'],
      scripts=['bin/cfautodoc'],
      install_requires=[
          'argparse',
      ],
      zip_safe=False)
