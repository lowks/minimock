from setuptools import setup, find_packages
import sys, os

version = '1.2.5'

try:
    doc_dir = os.path.join(os.path.dirname(__file__), 'docs')
    index = open(os.path.join(doc_dir, 'index.txt')).read()
    changelog = open(os.path.join(doc_dir, 'changelog.txt')).read()
    long_description = '\n'.join((index, changelog))
except IOError:
    long_description = 'Please see docs/index.txt for more info'

setup(name='MiniMock',
      version=version,
      description="The simplest possible mock library",
      long_description=long_description,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
      ],
      keywords='mock testing unittest',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://pypi.python.org/pypi/MiniMock',
      license='MIT',
      #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      py_modules=['minimock'],
      zip_safe=True,
      )
