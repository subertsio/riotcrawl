import setuptools 


with open('README.rst', 'r') as f:
    long_description = f.read()


REQUIRES = [
        'scrapy',
        ]



setuptools.setup(
        name='riotcrawl',
        version='0.0.1.dev1',
        author='NONAMES',
        long_description=long_description,
        packages=setuptools.find_packages(),
        install_requires=REQUIRES,
        python_requires='>=3',
        )
