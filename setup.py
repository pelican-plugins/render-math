#!/usr/bin/env python

from setuptools import find_packages, setup

exec(open("pelican/plugins/render_math/version.py").read())

setup(
    name="pelican-render-math",
    version=__version__,  # NOQA F821
    author="Pelican Dev Team",
    author_email="authors@getpelican.com",
    packages=find_packages(),
    url="https://github.com/pelican-plugins/render-math",
    license="AGPL-3.0",
    description="Render Math Plugin for Pelican",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["pelican>=4.3", "typogrify>=2.0.7"],
    include_package_data=True,  # includes files from MANIFEST.in if in render_math/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pelican :: Plugins",
        "Framework :: Pelican",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
    ],
)
