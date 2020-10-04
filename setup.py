from setuptools import setup

setup(
    name='comp_sec',
    packages=['comp_sec', 'comp_sec.algs'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)