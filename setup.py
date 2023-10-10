from setuptools import setup

setup(
    name='typeform-pre-commit',
    description='Pre-commit hooks for Typeform',
    url='https://github.com/Typeform/typeform-pre-commit',
    version_format='{tag}+{gitsha}',

    author='Contributors',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'setuptools-git-version',
    ]
)
