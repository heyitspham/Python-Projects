
class ProtectedVar:
    def __init__(self):
        self._protected_var = 0

object1 = ProtectedVar()
object1._protected_var = 34
print(object1._protected_var)

class PrivateVar():
    def __init__(self):
        self.__private_var = 12

    def printPrivateVar(self):
        print(self.__private_var)

    def setPrivateVar(self, private):
        self.__private_var = private

object2 = PrivateVar()
object2.printPrivateVar()
object2.setPrivateVar(32)
object2.printPrivateVar()
