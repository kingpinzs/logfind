try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'logfind',
    'author': 'Jeremy',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'no@email.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)
