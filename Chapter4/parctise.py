# Q1
import math

l1 = []

# for i in range(4):
#     num = int(input("Enter the number: "))
#     l1.append(num)

# if(l1[0]>l1[1] and l1[0]>l1[2] and l1[0]>l1[3]):
#     print(f"The greatest number is 1 {l1[0]}")
# elif(l1[1]>l1[0] and l1[1]>l1[2] and l1[1]>l1[3]):
#       print(f"The greatest number is 2 {l1[1]}")
# elif(l1[2]>l1[0] and l1[2]>l1[1] and l1[2]>l1[3]):
#       print(f"The greatest number is 3 {l1[2]}")
# else:
#      print(f"The greatest number is 4 {l1[2]}")


# Q2

# total_marks_per_subject = 100
# no_of_suject = 5
# sum_of_the_numbers = 0

# for i in range(no_of_suject):
#     number = int(input(f"Enter your makrs for subject {i+1}: "))
#     percentage = (number/total_marks_per_subject)*100
#     print(percentage)

#     if(percentage>=33):
#         sum_of_the_numbers += number
#     else:
#         print(f"Bad Luck your falid in exam subject NO {i+1} ")

    

# total_percentage = (sum_of_the_numbers/(no_of_suject*total_marks_per_subject))*100

# if(total_percentage>=40):
#     print(f"Congratulations you are passed the exam successfully with the percentage of {total_percentage}")
# else:
#     print(f"Bad Luck your falid in exam {total_percentage}")     




# Q3 

# p1 = "Make lot of money"
# p2 = "subscribe us"
# p3 ="buy now"
# p4 = "claim now"

# comment = input("Enter your comment: ")

# if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
#     print("This comment is a spam")

# else:
#     print("This comment is not a spam")


# Q4 

# password = input("Enter your Password: ")

# if(len(password)<10):
#     print("Please enter the longer password")
# else:
#     print("Password is correct")



# Q5
# l1 = ["Abhishek","Divya","Kailash","Shaswat","Abahy"]

# name = input("Enter your name: ")

# if(name in l1):
#     print(f"Yes your name is in the list: Hello  {name}")
# else:
#     print(f"OOPS! Yes your name not in the list: Sorry {name}")


# Q6 

sentence = input("Enter your thoughts: ")

if("Abhishek".lower() in sentence.lower()):
    print("This sentence is talking about Abhishek")
else:
    print("This sentence is not talking about Abhishek")