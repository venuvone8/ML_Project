from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ML_Projects',
    version='0.0.1',
    author='Venu',
    author_email='venuvone8@gmail.com',
    packages=find_packages(),  # Use find_packages() for regular packages
    install_requires=get_requirements('requirements.txt'),
    long_description=open('README.md').read(),  # Optional: Add long description
    long_description_content_type='text/markdown',  # Optional: Specify the content type
)
