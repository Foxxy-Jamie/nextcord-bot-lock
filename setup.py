from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

VERSION = '0.0.12'
DESCRIPTION = 'Bot Check Ext so you can lock your bots to certain channels'
LONG_DESCRIPTION = 'Bot Check Ext so you can lock your bots to certain channels'

# Setting up
setup(
    name="nextcord-bot-lock",
    version=VERSION,
    author="Jamie Hogan",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['nextcord.py', 'aiosqlite'],
    keywords=['python', 'nextcord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
