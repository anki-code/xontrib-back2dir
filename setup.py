#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-back2dir',
    version='0.1.2',
    license='MIT',
    author='anki-code',
    author_email='anki-code@no.no',
    description="Return to the most recently used directory when starting the xonsh shell.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py']},
    platforms='any',
    url='https://github.com/anki-code/xontrib-back2dir',
    project_urls={
        "Documentation": "https://github.com/anki-code/xontrib-back2dir/blob/master/README.md",
        "Code": "https://github.com/anki-code/xontrib-back2dir",
        "Issue tracker": "https://github.com/anki-code/xontrib-back2dir/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
