from setuptools import setup, find_packages
from gsxws.core import VERSION

setup(
    name="gsxws",
    version=VERSION,
    description="Library for communicating with GSX Web Services API.",
    long_description=open('README.rst').read(),
    install_requires=['PyYAML', 'lxml'],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP"
    ],
    keywords="gsx, python",
    author="Filipp Lepalaan",
    author_email="filipp@fps.ee",
    url="https://github.com/filipp/py-gsxws",
    download_url="https://github.com/filipp/py-gsxws/tarball/0.55",
    license="BSD",
    packages=find_packages(),
    package_data={'gsxws': ['products.yaml', 'langs.json']}
)
