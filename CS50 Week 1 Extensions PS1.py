'''In a file called extensions.py, implement a program that
prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.'''

file_name = str(input("What is the name of the file?"))
split_name = file_name.split(".")

if ".gif" in file_name.lower():
    print(split_name[0] + "/gif")
elif ".jpg" in file_name.lower():
    print(split_name[0] + "/jpg")
elif ".png" in file_name.lower():
    print(split_name[0] + "/png")
elif ".pdf" in file_name.lower():
    print(split_name[0] + "/pdf")
elif ".txt" in file_name.lower():
    print(split_name[0] + "/txt")
elif ".zip" in file_name.lower():
    print(split_name[0] + "/zip")
else:
    print("application/octet-stream")
