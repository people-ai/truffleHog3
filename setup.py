"""Distribution settings."""

import pathlib

from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="pai-truffleHog3",
    version="2.0.1.2",
    packages=["truffleHog3", "truffleHog3.lib"],
    license="GNU",
    description="Find secrets in your codebase.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/peopleai/truffleHog3",
    author="Mike Urbanski",
    author_email="mike@people.ai",
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["GitPython==3.1.0", "jinja2==2.11.1", "PyYAML==5.3.1"],
    entry_points={"console_scripts": ["trufflehog3 = truffleHog3.cli:run"]},
)
