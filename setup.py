# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agent-guard",
    version="0.1.0",
    author="Raj Parmar",
    author_email="rajparmar2308@gmail.com",
    description="An operational monitoring library for Crew AI applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajparmarr2308/agent-guard", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "psutil",
        "matplotlib",
        "streamlit",
        "tiktoken"
    ],
    include_package_data=True,
    package_data={
        # Include any additional files here
    },
)
