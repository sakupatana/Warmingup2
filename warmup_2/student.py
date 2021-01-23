class Student:

    def __init__(self, name, student_id):
        self.__name = name
        self.__id = student_id
        self.__credits = []


    def add_credits(self, newlist):
        self.__credits += newlist


    def get_name(self):
        return self.__name


    def get_id(self):
        return self.__id


    def get_credits(self):
        return self.__credits

    def get_sum(self):
        credits_sum = sum(self.__credits)
        return credits_sum
