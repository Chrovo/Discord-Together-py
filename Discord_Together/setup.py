from setuptools import setup, find_packages

setup(
        name="Discord-Together-py",
        author="Chrovo",
        version="0.0.1",
        description = "This is a package that is ideally used with discord.py, it allows you to do different activities in voice chat",
        #long_description = open("README.md").read(),
        url = "https://github.com/Chrovo/Discord-Together-py",
        classifiers = ["Intended Audience::Developers", "Programming Language::Python", "Natural Language::English","Programming Languuage::Python::3"],
        install_requires = ['discord.py','aiohttp'],
        license = "MIT",
        packages = find_packages(),
        keywords="discord-together"
)
