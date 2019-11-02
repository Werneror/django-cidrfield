from setuptools import setup, find_packages
import sys, os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import cidrfield

setup(
    name="django-cidrfield",
    version=cidrfield.__version__,
    url="https://github.com/Werneror/django-cidrfield",
    author="Werner",
    author_email="me@werner.wiki",
    license="MIT",
    description="Proper CIDR fields for Django running on any database",
    long_description=open('README.rst').read(),
    keywords="ip, cidr, models, django",
    packages=["cidrfield"],
    setup_requires=["setuptools"],
    install_requires=("setuptools", "django",),
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",),
)

