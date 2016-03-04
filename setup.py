from setuptools import setup


setup(name='cfautodoc',
      version='0.1.4',
      description='Tool to document CloudFormation templates in Markdown.',
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
