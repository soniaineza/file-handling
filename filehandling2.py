file_write= open('filehandling2.txt','w')
print("opening the file in write mode")
file_write.write("Hello my name is sonia")
file_write.close()

file_read=open('filehandling2.txt','r')
print("opening the file in read mode")
print(file_read.read())
file_read.close()

file_append= open('filehandling2.txt','a')
print("opening the file in append mode")
file_append.write("\nI'm from rwanda")
file_append.close()