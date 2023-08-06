from setuptools import find_packages, setup

E_DOT = "-e ."
def getRequirements(file: str) -> list[str]:
    requirements = []
    with open(file) as fileObject:
        requirements = fileObject.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements
    

setup(
    name="MLBasics",
    version="1.0.0.0",
    author="cadaats",
    packages=find_packages(),
    install_requires=getRequirements("requirements.txt")
)