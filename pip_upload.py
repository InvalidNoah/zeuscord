import os

os.system('python3 setup.py sdist')
os.system('twine upload dist/*')