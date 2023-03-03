from sys import platform, version, exit as eexit
from os import mkdir, system, listdir, remove
from importlib import import_module
from urllib.request import urlopen
from urllib.error import URLError
from shutil import move, rmtree
from time import perf_counter
from json import load, dumps
from zipfile import ZipFile
from os.path import exists
from time import time


try:
    ipath:   str = input('Installation path (Press enter to skip): ')
    start: float = perf_counter()
    path:    str = '/'.join(__file__.split('/')[0:3]) + '/Library/EzMusic/'
    pyv:    list = version.split(' ', 1)[0].split('.')[0:2]
    version: str = '1.0.0'
    added:  bool = False

    def exit(code: int, details: str=''):
        print(details)
        eexit(code)

    print('\n')
    if __name__ != '__main__':
        exit(1)
    elif platform != 'darwin':
        exit(1, 'You need MacOS to install EzMusic!')
    elif int(pyv[0]) == 3 and int(pyv[1]) < 10:
        exit(1, 'You need python 3.10 or above \nYou currently have version {0}'.format('.'.join(pyv)))
    elif not exists(path):
        added: bool = True
        mkdir(path)
        with open(path + 'data.json', 'a+') as _f:
            epoch: str = str(time())
            json:  str = (
                        '{\n' + 
                        '  "firstInstalled": ' + epoch + ',\n' +
                        '  "newID": 1,\n' + 
                        '  "installed": {\n' +
                        '    "0": {\n' + 
                        '      "date": ' + epoch + ',\n' + 
                        '      "version": "' + version + '"\n' +
                        '    }\n' + 
                        '  }\n' +
                        '}'
                        )
            _f.write(json)
    elif not added:
        try:
            with open(path + 'data.json', 'r+') as _f:
                sdata: dict = load(_f)
                sdata['newID'] += 1
                sdata['installed'][str(sdata['newID'])] = {"date": time(), "version": version}
                _f.seek(0)
                _f.truncate(0)
                _f.write(dumps(sdata, indent=2))
        except FileNotFoundError:
            with open(path + 'data.json', 'a+') as _f:
                pass
            exit(1, 'An error occured, please retry.')

    # No effective way to install packages from inside a script
    with open('requirements.txt', 'a+') as _f:
        _f.write('Cython\nkivy\npyobjc\npyperclip\npytube\ntooltils')

    system('pip install -r requirements.txt')
    system('pip3 install -r requirements.txt')
    try:
        import_module('tooltils')
        remove('requirements.txt')
    except ImportError:
        exit(1, 'Please install requirements.txt manually')

    # Grab files from archive file
    # Not standard because it isn't reliable and could stop working
    # Looking for a way to grab indiviual versions of the repo
    # Without third party libraries like PyGithub
    try:
        data: bytes = urlopen('https://github.com/feetbots/ezmusic/archive/master.zip', timeout=10).read()
    except URLError:
        exit(1, 'An error occured while fetching the latest version of EzMusic.')
    with open(ipath + 'files.zip', 'wb') as _f:
        _f.write(data)
    with ZipFile(ipath + 'files.zip') as _f:
        _f.extractall(ipath + 'ezmusic')
    for i in listdir(ipath + 'ezmusic/ezmusic-home/'):
        if i == 'INFO':
            with open(ipath + 'ezmusic/ezmusic-home/INFO') as _f:
                data:    list = _f.readlines()
        elif i not in ['LICENSE', 'INFO', 'README.md', 'requirements.txt']:
            move(ipath + 'ezmusic/ezmusic-home/' + i, ipath + 'ezmusic/')
    remove(ipath + 'files.zip')
    rmtree(ipath + 'ezmusic/ezmusic-home/', ignore_errors=True)

    with open(ipath + 'ezmusic/config.json', 'a+') as _f:
        json: str = (
                     '{\n' +
                     '  "installed": ' + str(time()) + ',\n' + 
                     '  "autoUpdate": true,\n' + 
                     '  "version": "1.0.0",\n' + 
                     '  "boot": "gui",\n' +
                     '  "id": ' + str(sdata['newID'] + 1) +'\n' + 
                     '}'
                    )
        _f.write(json)

    taken: float = round(perf_counter() - start, 3)
    print('Setup finished.',
          '- Installed in {}'.format('"' + ipath + '"'
                                     if ipath else 'Current Directory'),
          '- Version: {}({})'.format(data[0].splitlines(False)[0], data[1].splitlines(False)[0]),
          '- Took {}s'.format(taken),
          sep='\n')
except KeyboardInterrupt:
    exit(1, '')
