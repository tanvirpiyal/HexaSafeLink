from setuptools import setup, find_packages

setup(
    name="hexasafelink",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "colorama",
        "tldextract",
        "dnspython",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "hexasafelink=hexasafelink.cli.main:main",
        ],
    },
    author="Tanvir",
    author_email="youremail@example.com",
    description="HexaSafeLink CLI - Your Shield Against Scam Links",
    url="https://github.com/yourusername/HexaSafeLink",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
