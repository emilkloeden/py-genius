from setuptools import setup

setup(
    name='py_genius',
    version='0.3.0',
    description='A thin wrapper around the Genius API',
    author='Emil Kloeden',
    author_email='emilkloeden@gmail.com',
    url='https://github.com/emilkloeden/py-genius',
    download_url='https://github.com/emilkloeden/py-genius/0.3.0.tar.gz',
    keywords=['genius'],
    classifiers=[],
    tests_require=['pytest'],
    install_requires=['requests>=2.13.0'],
    packages=['py_genius']
)
