class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks
    def display_info(self):
        print("\nStudent Information")
        print(f"Name: {self.__name}")
        print(f"Roll_no: {self.__roll_no}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.calculate_grade()}")
    def calculate_grade(self):
        if self.__marks >=90:
            return "Grade A"
        elif self.__marks >=80:
            return "Grade B"
        elif self.__marks >=70:
            return "Grade C"
        elif self.__marks >= 60:
            return " Grade D"
        else:
            return " Grade F"
        
student=Student("Zainab",21,91)
student.display_info()
student.calculate_grade()