from setuptools import setup

version = None
with open('guildwars2/consts.py', 'r') as f:
    for line in f.readlines():
        if 'version' in line:
            version = line.split('=')[1].replace('"', '').replace("'", '').strip()

install_requires = [
    'requests'
]

setup(name='python-guildwars2',
    version=version,
    description="Guild Wars 2 Python Binding",
    author='Jason Straw',
    author_email='jason.straw@gmail.com',
    url='http://github.com/jstraw/python-guildwars2/',
    install_requires=install_requires,
)
