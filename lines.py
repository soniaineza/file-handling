file = open('codingal.txt','r')
counter = 0
content=file.read()
colist=content.split('\n')
for i in colist:
    if i:
        counter=counter+1
print("The number of lines in the file are",counter)
