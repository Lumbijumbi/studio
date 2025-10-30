"""Setup configuration for the Python LoliCode generator."""

from setuptools import setup, find_packages

setup(
    name='lolicode-generator',
    version='1.0.0',
    description='Python implementation of LoliCode script generator for OpenBullet 2 with GUI',
    author='HAR2LoliCode',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    scripts=['gui_app.py'],
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        'test': [
            'pytest>=8.0.0',
            'pytest-asyncio>=0.23.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'lolicode-gui=gui_app:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
