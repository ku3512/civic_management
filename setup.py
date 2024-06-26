from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in civic/__init__.py
from civic import __version__ as version

setup(
	name="civic",
	version=version,
	description="Civic is a powerful mobile application designed to foster community engagement",
	author="Nitesh",
	author_email="nitesh@123",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
