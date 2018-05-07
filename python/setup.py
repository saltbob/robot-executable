from setuptools import setup, find_packages

REQUIREMENTS = open("requirements.txt").readlines()

setup(
    name='robot-executable',
    version='1.0.0',
    description='Demonstrate how to use pyinstaller for Robot Framework.',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'run_robot=robot_executable.run:main'
        ],
    }
)
