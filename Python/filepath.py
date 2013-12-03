# conding =utf8

import sys, os
def getpath():
    path_getcwd = os.getcwd()
    path_realpath = os.path.split(os.path.realpath(__file__))[0]
    path_abspath = os.path.split(os.path.abspath(sys.argv[0]))[0]
    path_syspath = sys.path[0]
    print('path_getcwd is:'  + path_getcwd)
    print('path_realpath is:' + path_realpath)
    print('path_abspath is: ' + path_abspath)
    print('path_sys is:' + path_syspath)

if __name__ == '__main__':
    getpath()