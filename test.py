class Vs:
    def execute(self):
        print('vs code')

class Py():
    def execute(self):
        print('py charm')


class Laptop:
    def editor(self, ide):
        ide.execute()


lap1 = Laptop()
ide = Vs()
lap1.editor(ide)