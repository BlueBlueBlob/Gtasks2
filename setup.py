import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'gtasks2',
    version = "0.1.0",
    description = 'A fork from the greatest gtasks ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'BlueBlueBlob',
    author_email = 'adrien.lesot@gmail.com',
    url = 'https://github.com/BlueBlueBlob/Gtasks2',
    license = 'MIT',
    install_requires = [
        "keyring",
        "requests_oauthlib"
    ],
    packages= setuptools.find_packages(),
    package_data = {'':['*.json']},
    keywords = ['google', 'tasks', 'task', 'gtasks', 'gtask']
)
