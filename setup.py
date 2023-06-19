import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoyt",
    version="0.0.1",
    author="Maciej Ułanowicz",
    description="Python script for quickly searching and downloading new content out of YouTube.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: AGPL V3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["ytscheduler"],
    package_dir={'':'ytsheduler/src'},
    install_requires=['yt-dlp']
)