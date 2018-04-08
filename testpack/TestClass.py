# coding=utf-8

class a:
    def __init__(self):
        """ init """
        self.m = 1

    def add(self):
        """add function"""
        self.p = 4
        print(self.p + self.m)


class b(a):
    def __init__(self):
        a.__init__(self)
        self.mm()
        self.n = 2

    def sum(self):
        print(self.m + self.n)

    def mm(self):
        print "mm"
        self.m = 8
        self.__p()

    def __p(self):
        print "private func"

    def __ee__(self):
        print "exception"
        try:
            fu()
        except Exception, e:
            print e.message

    def passTest(self):
        pass

    def ifpass(self):
        if 1 == 2:
            pass


c = b()
c.sum()

c.add()
c.__ee__()
c.mm()
