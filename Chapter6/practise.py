
# Q1 

# def findGratest():
#     num1 = int(input("Enter your namuber: "))
#     num2 = int(input("Enter your namuber: "))
#     num3 = int(input("Enter your namuber: "))
#     if(num1>num2 or num1>num3):
#         return f"The Gratest number in all is num1:  {num1}"
#     elif(num2>num1 or num2>num3):
#         return f"The Gratest number in all is num2:  {num2}"
#     else:
#         return f"The Gratest number in all is num3:  {num3}"
    

# print(findGratest())


# Q2 

# def frehrn_to_cellicius():
#     f = int(input("Enter the tempreture: "))
#     return round(5*(f-32)/9,2)

# print(frehrn_to_cellicius())


# Q3
# n = int(input("Enter your number: "))

# def find_sum_natural_numbers(n):
 
#     if n==0 :
#         return 0
#     else:
#         return n+find_sum_natural_numbers(n-1)



# print("Sum =", find_sum_natural_numbers(n))


# Q4

# def pattern(n):
#     if(n==0):
#         return 
#     print("*"*n)
#     pattern(n-1)

# pattern(5)


# Q5 

# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#         return n

# l = ["Abhishek","viashl","kamal","al"]

# print(rem(l,"bh"))

# Q6 

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(1099)