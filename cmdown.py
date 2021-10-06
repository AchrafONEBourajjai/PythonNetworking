from cmd import Cmd
class Myprompt(Cmd):
    def do_exit(self,inp):
        print('bye')
        return True
    def do_add(self,inp):
        print("adding {}".format(inp))
    def do_out(self,inp):
        print('out')
Myprompt().cmdloop()
print("after")