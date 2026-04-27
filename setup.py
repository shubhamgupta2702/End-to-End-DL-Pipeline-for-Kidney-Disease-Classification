from setuptools import find_packages, setup

setup(
    name="End to End DL Pipeline for Kidney Disease Classification",
    version="0.0.1",
    author="Shubham Gupta",
    author_email="shubhamgupta43567@gmail.com",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "fastapi",
        "uvicorn",
        "python-dotenv", 
        "pathlib"
    ]
)