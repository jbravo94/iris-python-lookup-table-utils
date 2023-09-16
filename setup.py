from setuptools import setup, find_packages

setup(
    name='pylotaut',
    version='1.0.0',
    description='IRIS Python Lookup Table Utils',
    author='Johannes Heinzl',
    author_email='jh.heinzl@gmail.com',
    url='https://heinzl.dev/',
    packages=find_packages(include=['pylotaut', 'pylotaut.*']),
    install_requires=[
        'openpyxl'
    ]
)