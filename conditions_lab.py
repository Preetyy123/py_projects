"""a = input("Enter the first num: ")
b = input("Enter the 2nd num: ")
c = input("Enter the 3rd num: ")

if a > b and a > c:
    print(a, "is largest value")

elif b > a and b > c:
    print(b, "is a largest numb")

else:
    print(c, "is the largest value")"""

#take the input from user and store it in list then take the num for mulplication from user and multiply those numbers and store it in list.
"""i = 1
j = int(input("Enter the num for multiply:"))
list1 = []
list2 = []
while i <= 5:
    x= int(input("Enter num:"))
    y = x*j
    list1.append(x)
    list2.append(y)
    i += 1
print("this is the list1:", list1)
print("this is the list2 after multiply:", list2)"""

#create a list, input 1 num from user and multiple it with all values present in list and store the output in another list.
"""list1 = [10, 20, 30, 40, 50]
list2 = []
x = int(input("Enter a num: "))
i = 0
print(list1)
while i <= len(list1):
    y = list1[i] * x
    list2.append(y)
    i += 1

print(list2)"""

#take a list input from user and count how many even and odd are there
"""i = 0
even1 = 0
odd1 = 0
list1 = []
while i <= 5:
    x = int(input("Enter Number: "))
    list1.append(x)
    if list1[i]%2 == 0:
        even1 += 1
    else:
        odd1 += 1
    i += 1
print(list1)
print(even1)
print(odd1)
"""
"""num = 19
div = 5

quotient = num//div
remainder = num - (quotient * div)
print(remainder)

print(num % div)"""

"""i = 0
list1 = ['preeti', 'teena', 'ali']
for name in list1:
    if name == 'ali':
        print('name exists at index:',i , name)
    i += 1

i = 0
list1 = ['preeti', 'teena', 'ali']
while i < len(list1):
    if list1[i] == 'ali':
        print("found at index", i, list1[i])

    i += 1"""

#loop a list using built-in function called map.
"""usernames = ['preeti', 'teena', 'lavisha', 'soorya']
def user1(item):
    print(item)
    return f"Hello {item}"

newuser = list(map(user1, usernames))
print(newuser)"""

"""list1 = [10, 20, 30, 40, 50, 60]
def multi(item):
    return item * 2
list2 = list(map(multi, list1))
print(list2)"""


#Create a setudent app, first add entries of four students
#add a new student
#update some details of any one student
#delete one student
#print the remaining subjects with student id's

"""
students = [{
    'id': 10,
    'class': 10,
    'subject': 'maths',
    'age' : 20
},
{
    'id': 20,
    'class': 20,
    'subject': 'science',
    'age' : 20
},
{
    'id': 30,
    'class': 30,
    'subject': 'phy',
    'age' : 20
},
{
    'id': 40,
    'class': 40,
    'subject': 'chem',
    'age' : 20
},

]

id = int(input("Enter your ID"))
class1= int(input("Enetr your class"))
sub = input("Enter your subject")
age = int(input("Enter your age:"))

newstu = {
    "id": id,
    'class': class1,
    'subject': sub,
    'age': age
}

students.append(newstu)
newId = int(input('Enter a new id'))
def updStu(item):
    if item['id'] == newId:
        return {
            'id': item['id'],
            'class': item['class'],
            'subject': 'Pre-Engineering',
            'age' : item['age']
        }
    else:
        return item
    
students = list(map(updStu, students))
print(students)

delStu = int(input("Enter ID; "))
def deleteStu(item1):
   if item1["id"] != delStu:
       return item1
   
students = list(filter(deleteStu, students))
print(students)

for student in students:
    print("Total Subjects", student['subject'], "with students Ids", student['id'])"""

# Check the largest and smallest num in list
"""list1 = [4, 55, 8, 98, 111, 20, 200]
largest = list1[0]
smallest = list1[0]

for num in list1:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(list1)
print('largest num is:', largest)
print('smallest num is:', smallest)"""

#format function
"""num = 39
mult = 10 * num

print(f"2 * {num} = {mult}")"""

#Modules
#import os

"""currentDir = os.getcwd()
print(f"cureent directory is {currentDir}")

filelist = os.listdir()
print(filelist)"""

"""import ipaddress
x = ipaddress.ip_network()
print(x)"""

"""class student:
    def __init__(self, fullname):
        self.name = fullname
#        print(f"Full name is {self.name}")

s1 = student("Preeti")
print(f"Full name is {s1.name}")"""

#default constructor
"""class student:
    def __init__(self):
        pass

#parameterized Constructor
class student:
    def __init__(self, fullname):"""

"""class student:
	CollName = "QUEST" #class attribute, constant
	
	def __init__(self, name, marks):
		self.name = name  #object attribute, can change the value
		self.marks = marks
		
	def avgStu(self):
		sum += 0
		for num in self.marks:
		    sum += num
		print("the avrege is ", sum/3)
s1 = student("preeti", [80, 90, 100])
print(s1.name, s1.avgStu)"""

#Create account class with two parameters balance and account num then create methods for debit, credit, and total amount
"""
class Account:
    def __init__(self, balance, AccNo):
        self.balance = balance
        self.AccNo = AccNo

    def debit(self, deduct):
        self.balance -= deduct
        print(deduct, "is debited from your account")
    
    def credit(self, cred):
        self.balance += cred
        print(cred, "is credited from your account")

    
    def totalBal(self):
        print("This is your total balance now: ", self.balance)

Acc = Account(25000, 123456)
Acc.debit(5000)
Acc.credit(7000)
Acc.credit(10000)
Acc.totalBal()"""

#make private method and call it and pass it a argument within class from diff method then call it.
"""class student:
    def __init__(self, Stuname):
        self.Stuname = Stuname
        print("Hello ", self.Stuname)
    def __StuPass(self, passw):
        self.passw = passw
    def StuDetails(self):
        self.__StuPass(12345678)
        print(self.Stuname, "Your Password is: ", self.passw)

s1 = student("preeti")
s1.StuDetails()"""

"""NB_URL = ''
NB_Token = ''

import ipaddress
import pynetbox

try:
    nb = pynetbox.api(URL = NB_URL, TOKEN = NB_Token)
    nb.http_session.verify = False   # Set to True if your NetBox uses a trusted SSL certificate

except Exception as e:
    print(f"Error connecting to NetBox {NB_URL}")

net = ipaddress.ip_network("2400:ADC0:0000::/32")

try:
    for subnet in net.subnets(new_prefix= 48):
        

except Exception as e:"""
    

x = 'preety'

print(x.upper())