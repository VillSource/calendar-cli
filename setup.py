from setuptools import setup
setup(
    name = 'calendar-cli-kku',
    version = '0.0.0',
    packages = ['calendarcli'],
    description='test file',
    long_description="lone desc",
    url = "https://github.com/VillSource/calendar-cli",
    package_dir={'data': 'calendarcli/data'},
    package_data={'data': ['calendarcli/data/*']},
    include_package_data=True,
    install_requires=[
        'colorama',
    ],
    entry_points = {
        'console_scripts': [
            'calendar = calendarcli.__main__:main',
            'calendar-cli = calendarcli.__main__:main',
            'ccal = calendarcli.__main__:main'
        ]
    })
