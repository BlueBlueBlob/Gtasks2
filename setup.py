import setuptools

setuptools.setup(
    name = 'gtasks2',
    version = "0.1.0",
    description = 'A fork from the greatest gtasks ',
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
