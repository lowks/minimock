from setuptools import setup

version = '1.2.8'

try:
    from os.path import join, dirname
    doc_dir = join(dirname(__file__), 'docs')
    index = open(join(doc_dir, 'index.rst')).read()
    changelog = open(join(doc_dir, 'changelog.rst')).read()
    long_description = '\n'.join((index, changelog))
except IOError:
    long_description = 'Please see docs/index.rst for more info'

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
    maintainer='Josh Bronson',
    maintainer_email='jabronson@gmail.com',
    url='http://pypi.python.org/pypi/MiniMock',
    license='MIT',
    py_modules=['minimock'],
    zip_safe=True,
    )
