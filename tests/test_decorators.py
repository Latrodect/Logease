from setuptools import setup, find_packages

setup(
    name="logless",  
    version="0.1.0",  
    description="A Python logging library designed to replace traditional logging mechanisms using decorators and modules.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Hasan Bahadır Nural",
    author_email="bahadir.nural@outlook.com",
    url="https://github.com/Latrodect/logless",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[ ],
    include_package_data=True,  
)
