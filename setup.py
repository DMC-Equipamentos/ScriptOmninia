from setuptools import setup, find_packages

setup(
        name='OmniaScript', 
        version='1.0', 
        entry_points = {
            'console_scripts': ['do_omnia=OmniaScript.run:main',],
        },
        install_requires = [
            'pandas',
        ],
        packages=find_packages())
