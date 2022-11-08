from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A wrapper for the site lasagna.email"
LONG_DESCRIPTION = "A wrapper for the site lasagna.email"

setup(
    name="lasagnamail",
    version=VERSION,
    author="TheBaconPug",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],

    keywords=["python", "email", "lasagna", "tempmail", "disposable email", "lasagnamail"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)