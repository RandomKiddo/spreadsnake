from setuptools import setup

rst = []
with open('README.rst', 'r') as f:
    for line in f:
        rst.append(str(line))

ld = ''
for i in rst:
    ld += i + '\n'

setup(
    name = 'spreadsnake',
    packages = ['spreadsnake'],
    version = '1.0a1',
    license = 'MIT',
    description = 'A python spreadsheet api',
    long_description = ld,
    author = 'RandomKiddo',
    author_email = 'nghugare2@outlook.com',
    url = 'https://github.com/RandomKiddo/spreadsnake',
    download_url = 'https://github.com/RandomKiddo/spreadsnake/archive/1.0a1.tar.gz',
    keywords = ['PYTHON', 'SPREADSHEETS', 'API'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',     
        'Programming Language :: Python :: 3.8',
    ]
)