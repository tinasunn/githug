from setuptools import setup, find_packages
setup(
    name='gitwrap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'gitpython',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'gitwrap=gitwrap.gitwrap:gitwrap',
        ],
    },
)