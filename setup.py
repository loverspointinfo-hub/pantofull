from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pan-verification-api",
    version="1.0.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="API for PAN to Mobile verification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pan-verification-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "flask>=2.3.2",
    ],
)