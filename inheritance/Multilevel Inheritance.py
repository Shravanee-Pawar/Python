class Grandfather:
    def show_grandfather(self):
        print("I am Grandfather")


class Father(Grandfather):
    def show_father(self):
        print("I am Father")


class Son(Father):
    def show_son(self):
        print("I am Son")


s = Son()

s.show_grandfather()
s.show_father()
s.show_son()
