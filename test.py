import csv

male = female = other= 0
with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        if line[1] == 'Male':
            male += 1
        elif line[1] == 'Female':
            female += 1
        else:
            other += 1
print(line)
print('Male: ', male, 
    ' Female: ', female, 
    ' Other: ', other)


















# f = open("test.txt", 'r')
# print(f.readline())

# f.close()
# f = open("test.txt", "w")
# f.write("I did not want to delete the content, but it got deleted.")
# f.close()
# open("onefile.txt", "a")
# # open("myfile.txt", "x")
# f = open("yourfile.txt", "w")
