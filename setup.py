from setuptools import setup

version = '1.2.9.dev0'

try:
    from os.path import join, dirname
    readme = open('README.rst').read()
    changelog = open('CHANGELOG.rst').read()
    long_description = '\n'.join((readme, changelog))
except:
    long_description = 'Please see https://bitbucket.org/jab/minimock for more info'

setup(
    name='MiniMock',
    version=version,
    description='The simplest possible mock library',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        ],
    keywords='mock testing unittest',
    author='Ian Bicking',
    author_email='ianb@colorstudy.com',
    maintainer='Low Kian Seong',
    maintainer_email='kianseong@gmail.com',
    url='https://bitbucket.org/jab/minimock',
    license='MIT',
    py_modules=['minimock'],
    zip_safe=True,
    )
