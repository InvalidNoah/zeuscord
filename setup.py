from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zeuscord',
    version='0.1.0',    
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='ZeusCord speeds up Discord bot developement a lot by providing tons of useful features and commands.',
    url='https://github.com/nsde/zeuscord',
    author='onlix',
    author_email='neostyxde@gmail.com',
    license='MIT',
    packages=['zeuscord'],
    install_requires=['discord.py>=1.0',
                      'PyNaCl',
                      'python-dotenv',              
                      ],

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
