__author__ = "tricci"
__date__ = "$4 mai 2015 07:38:23$"

from setuptools import setup, find_packages

setup (
       name='the-deployer.com Public Rest Api',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='tricci',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )