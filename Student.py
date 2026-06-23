class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.courses=[]
        print(f"My name is {self.name} and my student_id is {self.student_id}")

s1=Student("Zainab","Zainab_123")
s2=Student("Ali","Ali_098")
s3=Student("Noor Fatima","Noor Fatima_456")