from setuptools import setup

from calendarcli import GUI
def readme():
    with open("README.md") as f:
        return str(f.read())


setup(
    name = 'calendar-cli-kku',
    version = '0.0.a6',
    packages = ['calendarcli'],
    description='test file',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url = "https://github.com/VillSource/calendar-cli",
    install_requires=[
        'colorama', 
        'inquirer',
        'eel'   
    ],
    entry_points = {
        'console_scripts': [
            'calendar = calendarcli.__main__:main',
            'calendar-cli = calendarcli.__main__:main',
            'ccal = calendarcli.__main__:main',
            'gcal = calendarcli.calendargui.__main__:main',
            'anirut = calendarcli.typer_version:main',
            "ggg = calendarcli.GUI.app:start"
        ]
    })


if __name__ == '__main__':
    from calendarcli.data.setting import setConfig
    setConfig('calendar','ID','None')