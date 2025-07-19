from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requriements
    """

    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # reads lines from the files
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement!= "-e.":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

setup(
    name = "Network security",
    version="0.0.1",
    author="Mahesh",
    author_email="maheshkammineni@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()

)


