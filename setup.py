import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytex-lnxpy", # Replace with your own username
    version="1.0",
    author="Alireza Yahyapour",
    author_email="lnxpylnxpy@gmail.com",
    description="A tool for writing papers via python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
