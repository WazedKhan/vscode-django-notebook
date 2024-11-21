from setuptools import setup, find_packages

setup(
    name="vscode-django-notebook",
    version="0.1.0",
    description="A utility to easily use Django in VS Code Jupyter Notebooks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abdul Wajed Khan",
    author_email="wajed.abdul.khan@gmail.com",
    url="https://github.com/WazedKhan/vscode-django-notebook",
    packages=find_packages(),
    install_requires=[],  # No dependencies other than Django
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
    ],
    keywords="django jupyter vscode development",
)
