try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Final Project',
    'authors' : 'Anjali Raul Camile',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages' : ['Dataminer'],
    'name' : 'DataMining'
}

setup(**config)
