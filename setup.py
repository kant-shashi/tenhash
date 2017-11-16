from setuptools import setup


setup(
    name = 'tenhash',
    packages = ['tenhash'],
    include_package_data = True,
    install_requires = [
        'flask',
    ],
)