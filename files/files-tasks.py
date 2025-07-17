# 1.Create a File  in "D:\\File Operations\\read.txt with "r" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
from itertools import count

f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read.txt", "r")
print(f.readable())
print(f.writable())
f.close()
print(f.close())

# 2.Create a File  in "D:\\File Operations\\write.txt with "w" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\write.txt","w")
print(f.readable())
print(f.writable())
f.close()
print(f.close())

# 3.Create a File  in "E:\\File\\append.txt with "a" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\append.txt","a")
print(f.readable())
print(f.writable())
f.close()
print(f.close())

# 4.Create a File  in "E:\\File\\append.txt with "x" mode and close file
#              a.Check whether file is readable or not?
#              b.Check whether file is writable or not?
#              c.Check whether file is closed or not?
# f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\append2.txt","x")
# print(f.readable())
# print(f.writable())
# f.close()
# print(f.close())

# Create a File  in "E:\\Python Notes\\read.txt with "W" mode and follow below steps
#              Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
#              Step 2: Close the file

f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read.txt","w")
f.write("Welcome to Greens Technology Java Class . Java is simple language .")
f.close()

# Create a File  in "E:\\Python Notes\\read.txt with "a" mode and follow below steps
#              Step 1: Write "Welcome to Greens Technology Java Class . Java is simple language ." in that file
#              Step 2: Replace word java as Python
#              Step 2: Close the file
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read.txt","r+")
r = f.read()
new_txt = r.replace("Java","Python")
f.seek(0)
f.write(new_txt)
f.close()

# Create a File  in "E:\\Python Notes\\read.txt with "w" mode and follow below steps
#              Step 1: Write the below content in line by line
#                      Java Class
#                      Python Class
#                      Selenium Class
#                      Mobile Testing Class
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read2.txt","w")
f.writelines(["Java class\n","Python class\n","Selenium class\n","Mobile Testing class\n"])
f.close()

# Create a File  in "E:\\Python Notes\\read.txt with "a" mode and follow below steps
#              Step 1: Add the below content in line by line
#                      Api Testing
#                      Postman Tool
#                      Appium
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read2.txt","a")
f.writelines(["Api Testing\n","Postman Tool\n","Appium\n"])
f.close()

# Create a File  in "E:\\Python Notes\\read.txt with "w" mode and follow below steps
#              Step 1: Add the below Employee details as array of file
#                      [100,vel,vel@gmail.com]
#                      [200,Nisha,Nisha@gmail.com]
#                      [300,Bala,Bala@gmail.com]
#                      [400,Ganesh,Ganesh@gmail.com]
f = open(r"C:\Users\Vasanth\PycharmProjects\Files - Task\files\read3.txt","w")
f.writelines(["[100,vel,vel@gmail.com]\n","[200,Nisha,Nisha@gmail.com]\n","[300,Bala,Bala@gmail.com]\n","[400,Ganesh,Ganesh@gmail.com]"])
f.close()

# Write a file below content
             # Velmurugan currently focuses on teaching and delivering placement support for all his students,
             # During this training journey, He has taken 400+ batches through different modes (Online, classroom, corporate).
             # Worked with major IT companies such as Verizon, Infosys, Bank of America, as well as several smaller private companies in delivering high-quality training.
             # Through his innovative ideas, Velmurugan has also suggested many customer value adds to different private companies which helped in saving lot of efforts for different customers.
f = open("write.txt","w")
f.writelines(["Velmurugan currently focuses on teaching and delivering placement support for all his students,\n",
             "During this training journey, He has taken 400+ batches through different modes (Online, classroom, corporate).\n",
             "Worked with major IT companies such as Verizon, Infosys, Bank of America, as well as several smaller private companies in delivering high-quality training.\n",
             "Through his innovative ideas, Velmurugan has also suggested many customer value adds to different private companies which helped in saving lot of efforts for different customers.\n"])
f.close()

# Description :Read all content in file  uing read() method
f = open("write.txt","r")
c = f.read()
print(c)
f.close()

# Description :Read all content in file after 100th index
f = open("write.txt","r")
f.seek(100)
c = f.read()
print(c)
f.close()

# Description :Read all content in file after 100th index
f = open("write.txt","r")
c = f.readlines()
print(c)
f.close()

# Description :Copy Jpeg image from Local Disk D to Local Disk E
import shutil
shutil.copy(r"C:\Users\Vasanth\Downloads\test.jpg",r"C:\Users\Vasanth\Downloads\Video")
print("Image Copied")

# Copy one video Local Disk E to Local Disk D
import shutil
shutil.copy(r"C:\Users\Vasanth\Downloads\Screen Recording 2025-06-30 100004.mp4",r"C:\Users\Vasanth\Downloads\Video")
print("Video Copied")

# Description :Create a CSV File for 10 Employee Details
import csv
employees = [
    [101, "Vasanth", "vasanth@gmail.com", "HR"],
    [102, "Nisha", "nisha@gmail.com", "Finance"],
    [103, "Bala", "bala@gmail.com", "Marketing"],
    [104, "Ganesh", "ganesh@gmail.com", "IT"],
    [105, "Priya", "priya@gmail.com", "Admin"],
    [106, "Kumar", "kumar@gmail.com", "Support"],
    [107, "Divya", "divya@gmail.com", "R&D"],
    [108, "Arun", "arun@gmail.com", "Operations"],
    [109, "Keerthana", "keerthana@gmail.com", "Sales"],
    [110, "Saravanan", "saravanan@gmail.com", "Legal"]
]
with open("Hello.csv","w",newline='') as f:
    v = csv.writer(f)
    v.writerow(["ID", "Name", "Email", "Department"])
    v.writerows(employees)


# Read 10 Employee Details from CSV File
import csv
with open("Hello.csv","r",newline='') as f:
    reader = csv.reader(f)
    count = 0
    for i in reader:
        print(i)
        count += 1
        if count == 10:
            exit()

# Create a ZIp File with Following text File
#              Day1Task
#              Day2Task
#              Day3Task
from zipfile import *
with ZipFile("Hello.zip","w",ZIP_DEFLATED) as f:
    f.write("Hello.csv")
    f.write("append.txt")

