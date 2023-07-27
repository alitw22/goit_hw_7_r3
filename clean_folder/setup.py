from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_alitw',
    version='0.0.2',
    description='Sort files in accordance its extansion',   
    author='Andriy Lytvynenko',
    author_email='alitw@hotmail.com',      
    packages=find_namespace_packages(),  
    entry_points={'console_scripts': ['clean_folder = clean_folder.main:start']}
  
)