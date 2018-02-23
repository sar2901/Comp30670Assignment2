from setuptools import setup

setup(name="systeminfo",
	version="0.1",
	description="Basic system information for COMP30670",
	url="",
	author="Sybilla",
	author_email="sybilla.robertson@ucdconnect.ie",
	licence="GP3",
	packages=['systeminfo'],
	entry_points={
		'consol_scripts':['comp30670_systeminfo=systeminfo.main:main']
		}
	)
