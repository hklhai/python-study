# coding=utf-8
import os


def myfork():
    """
    only support on Linux
    :return:
    """
    pid = os.fork()
    if pid == 0:
        print "this is child %d" % pid
    else:
        print "this is parent %d" % pid

if __name__ == '__main__':
    myfork()

