from distutils.core import setup

setup(
    name='chrono',
    description='A natural language date parser',
    version='0.0.1',
    author='Wanasit Tanakitrungruang',
    license='LICENSE.txt',
    packages=['chrono', 'chrono.parsers', 'chrono.parsers.*'],
    url='https://github.com/wanasit/chrono-python',
    download_url='https://github.com/wanasit/chrono-python/tarball/0.0.1',
    keywords = ['parser', 'time', 'date', 'natural'],
    install_requires=[]
)