class vs:
    def execute(self):
        print('vs code')

class Py():
    def execute(self):
        print('py charm')


class Laptop:
    def editor(self, ide):
        ide.execute()


lap1 = Laptop()
ide = vs()
lap1.editor(ide)