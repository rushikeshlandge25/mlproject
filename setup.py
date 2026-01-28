from setuptools import setup, find_packages
from typing import List
import os

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    # 🔥 THIS IS THE FIX
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_path)

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="src",
    version="0.0.1",
    author="Rushikesh",
    author_email="rushirlandge@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
'''
pip install -e .
        ↓
pip copies project to temp folder
        ↓
setup.py runs
        ↓
setup.py finds its own location using __file__
        ↓
requirements.txt loaded correctly
'''