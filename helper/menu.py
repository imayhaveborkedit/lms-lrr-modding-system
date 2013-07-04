from collections import OrderedDict
import sys, types

class Menu(): # do something about funcs with args
    def __init__(self, optionlist):
        self.options = OrderedDict(optionlist).items()
        self.prefix = ''
        self.suffix = ''
        self.indent = 0
        self.indentaffectsprompt = True
        self.prompt = ''
        self.prepromptspacer = True
        self.postpromtspacer = True
        self.defaultoption = None
        self.invalid = 'Invalid option.\n'
        self.repeatoninvalid = True
        self.executeonreturn = False

        for opt in self.options:
            if not isinstance(opt[1], (types.FunctionType, types.MethodType, types.GeneratorType)):
                raise TypeError(str(opt[1]) + " is not a function: " + str(type(opt[1]))[1:-1])


    def __repr__(self):
        return str(self.options)


    def menutext(self):
        menutext = ''
        pos = 1
        for option in self.options:
            menutext += " " * int(self.indent)
            menutext += self.prefix + str(pos) + self.suffix + ": "
            menutext += str(option[0]) + "\n"
            pos += 1
        return menutext[:-1]


    def open(self):
        if self.repeatoninvalid:
            loopthing = True
            while loopthing:
                chosen = self._getmenuinput()
                if isinstance(chosen, (types.FunctionType, types.MethodType, types.GeneratorType)):
                    if self.executeonreturn: return chosen()
                    else: return chosen
                del chosen
                self.doinvalidthing()
        else:
            if self.executeonreturn: self._getmenuinput()()
            else: return self._getmenuinput()


    def doinvalidthing(self):
        print self.invalid


    def _getmenuinput(self):
        print self.menutext()
        if self.prepromptspacer: print
        if self.indentaffectsprompt:
            sys.stdout.write(' ' * self.indent)

        # rewrite to allow for number OR text
        if self.defaultoption is not None:
            sys.stdout.write("[%d]: " % self.defaultoption)
        sys.stdout.write(self.prompt)
        sys.stdout.flush()

        try: o = int(sys.stdin.readline()[:-1])
        except KeyboardInterrupt: o = None
        except:
            if self.defaultoption is not None:
                o = self.defaultoption
            else: o = None
        if self.postpromtspacer: print
        return self.chooseoption(o)


    def chooseoption(self, optionnumber):
        try:
            optfunc = self.options[optionnumber-1][1]
        except (IndexError, TypeError) as e: return self.invalid
        return optfunc


def printtest1():
    print "test 1 works"

def printtest2():
    print "test 2 works"

def printtest3():
    print "test 3 works"

def testa():
    print "test a works"

def testb():
    print "test b works"


if __name__ == '__main__':
    def asdfasfd(): pass
    m2 = Menu([('Test a', testa),('Test b',testb)])
    m = Menu([('Test 1',printtest1),('Test 2',printtest2),('Test 3',m2.open)])
    m.executeonreturn = True
    m2.executeonreturn = True
    m.defaultoption = 3
    m2.defaultoption = 1
    f = m.open()
    if f is not None:
        if isinstance(f, basestring): print f
        else: f()
