from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_process_image",
    version="0.0.1",
    author="Quelvin",
    author_email="quelvincarvalho@gmail.com",
    description="Project DIO process image",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quelvin/package-template-dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)