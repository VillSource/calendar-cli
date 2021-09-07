from setuptools import setup
setup(
    name = 'calendar-cli',
    version = '0.1.0',
    packages = ['calendarcli'],
    package_data={'data': ['data/*']
    },
    entry_points = {
        'console_scripts': [
            'calendar = calendarcli.__main__:main',
            'calendar-cli = calendarcli.__main__:main',
            'ccal = calendarcli.__main__:main'
        ]
    })
