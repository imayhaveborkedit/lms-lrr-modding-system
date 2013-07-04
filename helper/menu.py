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
        self.promptspacer = True
        self.defaultoption = None
        self.invalid = 'Invalid option.\n'
        self.repeatoninvalid = True

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
                if isinstance(chosen, types.FunctionType):
                    return chosen
                del chosen
                self.doinvalidthing()
        else: return self._getmenuinput()


    def doinvalidthing(self):
        print self.invalid


    def _getmenuinput(self):
        print self.menutext()
        if self.promptspacer: print
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
        return self.chooseoption(o)


    def chooseoption(self, optionnumber):
        try:
            optfunc = self.options[optionnumber-1][1]
        except IndexError as e: return self.invalid
        return optfunc


##def printtest1():
##    print "test 1 works"
##
##def printtest2():
##    print "test 2 works"
##
##def printtest3():
##    print "test 3 works"
##
##
##if __name__ == '__main__':
##    def asdfasfd(): pass
##    m = Menu([('Test 1',printtest1),('Test 2',"derp"),('Test 3',printtest3)])
##    m.defaultoption = 3
##    f = m.open()
##    if isinstance(f, basestring): print f
##    else: f()
