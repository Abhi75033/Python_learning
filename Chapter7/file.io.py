# creating and writing the file 

# st = "Hey Abhishek you are a good Developer And made good and advanced project"

# w = open("file.txt","w")

# w.write(st)
# w.close()

# Reading the file


# append

# a = open('file.txt','a')

# st = "\nPoem completed and\n writen by Abhishek kumar"

# a.write(st)

# a.close()

# with keyword

with open("file.txt",'a') as f:
    st = "\nAbhishek is a good writer "
    f.write(st)
    

r = open('file.txt','r')

n = 5

red = r.readline()





while(red != ""):
    print(red)
    red = r.readline()

r.close()

# for lines in red:
#     print(lines)




