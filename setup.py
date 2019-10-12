#!/usr/bin/env python

from setuptools import setup, find_packages

exec(open('render_math/version.py').read())

setup(
    name='render_math',
    version=__version__,
    author='Jason K. Moore',
    author_email='moorepants@gmail.com',
    packages=find_packages(),
    url='http://github.com/pelican-plugins/render_math',
    license='AGPL-3.0',
    description='Math Render Plugin For Pelican',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
                      'pelican>=3.6',
                      'typogrify>=2.0.7',
                      ],
    include_package_data=True,  # includes files from MANIFEST.in if in render_math/
    classifiers=[
                 'Development Status :: 5 - Production/Stable',
                 'Framework :: Pelican :: Plugins',
                 'Framework :: Pelican',
                 'License :: OSI Approved :: GNU Affero General Public License v3',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python',
                 ]
)
