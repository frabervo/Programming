from setuptools import setup

setup(
    name='todolist_package',
    version='1.0',
    py_modules=['todolist'],
    include_package_data=True, 
    install_requires=[
        'click==8.1.3',
        'termcolor==1.1.0'
    ],
    entry_points={
        'console_scripts': [
            'todolist = todolist:main',
        ],
    },
)
