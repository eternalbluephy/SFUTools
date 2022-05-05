from distutils.core import setup
from setuptools import find_packages
 
setup(name = 'sfutools', 
      version = '1.0',
      description = 'Some simple, fast, and useful tools help you programming(Maybe).',
      long_description = '', 
      author = 'eternalbluephy',
      author_email = '',
      url = '',
      license = '',
      install_requires = [],
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
      ],
      keywords = '',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      include_package_data = True,
)
#!/usr/bin/env python
