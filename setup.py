import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'eagertools',
    version = '0.2',
    packages = find_packages(),

    # metadata for upload to PyPI
    author = 'Austin Bingham',
    author_email = 'austin.bingham@gmail.com',
    description = 'Eager version of some lazy functions.',
    license = 'MIT',
    keywords = 'functional',
    url = 'http://github.com/abingham/eagertools',
    downloadurl = 'http://pypi.python.org/pypi/eagertools',
    # long_description
    # zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
        ],
    platforms='any',
    include_package_data=True,
)
