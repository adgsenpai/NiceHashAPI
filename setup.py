from setuptools import setup, find_packages

setup(
    name="nicehash",
    version="0.0.1",
    author="Ashlin Darius Govindasamy",
    author_email="adgrules@hotmail.com",
    url="https://www.adgstudios.co.za",
    description="NiceHash Python API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT', 
    install_requires=["requests"]
)
