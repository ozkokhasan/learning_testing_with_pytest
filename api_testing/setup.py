from setuptools import setup, find_packages


setup(
    name='ozkokapitest',
    version='1.0',
    description="Practice API testing",
    author="Hasan Özkök",
    author_email='ozkokha@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "atomicwrites == 1.4.0",
        "attrs == 20.3.0",
        "certifi == 2020.12.5",
        "chardet == 4.0.0",
        "colorama == 0.4.4",
        "idna == 2.10",
        "iniconfig == 1.1.1",
        "more-itertools == 8.7.0",
        "oauthlib == 3.1.0",
        "ordereddict == 1.1",
        "ozkokapitest == 1.0",
        "packaging == 20.9",
        "pluggy == 0.13.1",
        "py == 1.10.0",
        "PyMySQL == 1.0.2",
        "pyparsing == 2.4.7",
        "pytest == 6.2.2",
        "pytest-html == 3.1.1",
        "pytest-metadata == 1.11.0",
        "requests == 2.25.1",
        "requests-oauthlib == 1.3.0",
        "toml == 0.10.2",
        "urllib3 == 1.26.4",
        "wcwidth == 0.2.5",
        "woocommerce == 2.1.1"
    ]
)
