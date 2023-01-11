from Users.managers import CustomBaseUserManager

class REQUIREDFIELDS:
    USER = ["password"]

class SEARCHFIELDS:
    USER = ["phone_number", "id"]

class Manager:
    class OBJECTS:
        USER = CustomBaseUserManager()

    class SUBSETS:
        USER = CustomBaseUserManager()

class USERNAME:
    USER = 'phone_number'
