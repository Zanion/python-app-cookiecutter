from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.app_command }}",
    version='0.0.1',
    py_modules=["{{ cookiecutter.app_command }}"],
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['test']),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        {{ cookiecutter.app_command }}={{ cookiecutter.app_command }}.cli:cli
    ''',
)
