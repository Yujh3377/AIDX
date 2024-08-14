# Person이라는 클래스를 정의하고, 이 클래스에는 name과 age 속성을 가지며, 
# greet() 메소드를 통해 
# "Hello, my name is [name] and I am [age] years old."을 출력하는 
# 메소드를 추가하시오.

# Person 클래스 만듬
class Person:
    # name, age 가진 생성자 구현
    # self = 객체그자신, 객체자신이 가지고 있는 메소드 호출 인스턴스변수값 접근
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # greet 메소드 구현
    def greet(self):
        # greet메소드 호출하면 객체 내부의  self.name, self.age값 리턴
        # self.name,self.age 받아서 정해진 메세지 출력
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# person은 "name", 300 값 받으시오
person = Person("name", 300)
# 인자를 받지 않고 리턴값이 없는 (person) 호출
person.greet()
