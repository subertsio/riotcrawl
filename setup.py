import os
import sys
import setuptools 

HERE = os.abspath(os.path.dirname(__file__))

sys.path.insert(0, HERE)

with open('README.rst', 'r') as f:
    DESCRIPTION = f.read()


REQUIRES = [
        'scrapy',
        ]



setuptools.setup(
        name='riotcrawl',
        version='0.0.1.dev1',
        author='NONAMES',
        long_description=DESCRIPTION,
        packages=setuptools.find_packages(),
        install_requires=REQUIRES,
        python_requires='>=3',
        )
