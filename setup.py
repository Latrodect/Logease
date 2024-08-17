from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='logease',
    version='0.2.0',
    description='A Python logging library designed to replace traditional logging mechanisms using decorators and modules.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bahadir Nural',
    author_email='bahadir.nural@outlook.com',
    url='https://github.com/Latrodect/Logease',
    packages=find_packages(),
    install_requires=[
        'colorlog',
        'pysnmp'
    ],
    package_data={},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
