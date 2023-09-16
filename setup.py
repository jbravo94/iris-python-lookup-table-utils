from setuptools import setup, find_packages

setup(
    name='pylotaut',
    version='0.1.0',
    description='Setting up a python package',
    author='Johannes Heinzl',
    author_email='jh.heinzl@gmail.com',
    url='https://heinzl.dev',
    packages=find_packages(include=['pylotaut', 'pylotaut.*']),
    install_requires=[
        'openpyxl'
    ]
)