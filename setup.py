# setup.py

import os
from setuptools import setup, find_packages

def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mkdocs-svg2obj-plugin',
    version='0.1.0',
    description='A MkDocs plugin that converts markdown encoded svg images into obj elements.',
	long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown svg',
    python_requires='>=3.5',
    url='https://github.com/mrieg7734/mkdocs-svg2obj-plugin',
    author='Markus Riegler',
    author_email='https://github.com/mrieg7734/mkdocs-svg2obj-plugin',
	license='MIT',
    install_requires=[
		'mkdocs'
	],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'svg2obj = svg2obj.plugin:SvgToObjPlugin',
        ]
    }
)
