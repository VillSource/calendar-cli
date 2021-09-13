from setuptools import setup
def readme():
    with open("README.md") as f:
        return str(f.read())


setup(
    name = 'calendar-cli-kku',
    version = '0.0.a3',
    packages = ['calendarcli'],
    description='test file',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url = "https://github.com/VillSource/calendar-cli",
    package_dir={'data': 'calendarcli/data'},
    package_data={'data': ['calendarcli/data/*']},
    include_package_data=True,
    install_requires=[
        'colorama', 
        'inquirer'     
    ],
    entry_points = {
        'console_scripts': [
            'calendar = calendarcli.__main__:main',
            'calendar-cli = calendarcli.__main__:main',
            'ccal = calendarcli.__main__:main'
        ]
    })
