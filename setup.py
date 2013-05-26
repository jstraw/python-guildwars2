from setuptools import setup
from guildwars2.consts import version


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
