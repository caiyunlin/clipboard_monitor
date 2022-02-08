import pathlib
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="clipboard_monitor",
    version="1.0.5",
    description="Monitor Clipboard changes and trigger related actions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cylin2000/clipboard_monitor/",
    author="Calvin Cai",
    author_email="cylin2000@163.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["clipboard_monitor"],
    include_package_data=True,
    install_requires=[],
    entry_points={
    },
)

# pip install wheel
# pip install twine
# python .\setup.py sdist bdist_wheel
# python -m twine upload dist/*