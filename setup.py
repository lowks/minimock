from setuptools import setup, find_packages
import sys, os

version = '0.9'

doc_dir = os.path.join(os.path.dirname(__file__), 'docs')
index_file = os.path.join(doc_dir, 'index.txt')

setup(name='MiniMock',
      version=version,
      description="The simplest possible mock library",
      long_description=open(index_file).read().strip(),
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
