import os

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = open('zeuscord/requirements.txt', encoding="utf-8").read()

setup(
    name='zeuscord',
    version='0.1.1',    
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='ZeusCord speeds up Discord bot developement a lot by providing tons of useful features and commands.',
    url='https://github.com/nsde/zeuscord',
    author='onlix',
    author_email='neostyxde@gmail.com',
    license='MIT',
    packages=['zeuscord'],
    entry_points = {
        'console_scripts': [
            'zeuscord=zeuscord.cli:run'
        ],
    },
    install_requires=[requirements.split('\n')],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
