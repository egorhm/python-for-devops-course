class base1(object):
    def __init__(self):
        print "base1.__init__"

    def fun(self):
        print "base1.fun"

    def __del__(self):
        print "base1.__del__"


class base2(base1):
    def __init__(self):
        print "base2.__init__"
        super(base2, self).__init__()

    def fun(self):
        print "base2.fun"
        super(base2, self).fun()

    def __del__(self):
        print "base2.__del__"
        super(base2, self).__del__()
