from setuptools import setup

setup(
        name="Discord-Together-py",
        author="Chrovo",
        version="0.0.1",
        description = "This is a package that is ideally used with discord.py, it allows you to do different activities in voice chat",
        long_description = "This is a package designed for discord bots, its meant for you to be able to watch youtube together in a voice channel and do other activities together. This is inspired from RemyK888's discord together but for javascript. However, this package is for python. Ideally used with the discord.py wrapper.",
        url = "https://github.com/Chrovo/Discord-Together-py",
        classifiers = ["Intended Audience::Developers", "Programming Language::Python", "Natural Language::English","Programming Languuage::Python::3"],
        install_requires = ['discord.py','aiohttp'],
        license = "MIT",
        packages = ["Discord_Together"],
        keywords="discord-together"
)
