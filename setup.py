from setuptools import setup

with open("README.md", "r") as longdesc:
    long_description = longdesc.read()


setup(
    name="Loop Detection on Linked List",
    description="Detect loop on a linked list and avoid print it",
    long_description=long_description,
    author="Alexander Gomez",
    version="0.1.0",
    packages=["linked_list"],
)
