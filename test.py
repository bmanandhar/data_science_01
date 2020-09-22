#id,Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage
#['508146', 'Male', '41', '1', '29.0', '1', '1-2 Year', 'No', '27927.0', '124.0', '231']
import csv
import numpy as np
from scipy import stats

age_list = []
male = female = 0
with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #checking number of members by gender
    next(csv_reader) #skips header
    for line in csv_reader:
        if line[1] == 'Male': male += 1
        elif line[1] == 'Female': female += 1
        age_list.append(int(line[2]))
#prints total num of members
print('Total members: ', len(age_list))
#prints percentile 75
print('Percentile: ', np.percentile(age_list, 75))
#prints avg age of members
print('Average age: ', int(round(np.mean(age_list))))
#prints median age
print('Median age: ', np.median(age_list))
#prints mode of ages
print('Mode of ages: ', stats.mode(age_list))
#prints total male, female
print('Male: {}\nFemale: {}'.format(male, female))

# path = "F:\data\google_stock_data.csv"
# file = open(path)
# for line in file: print(line)


print(dir(csv))














# f = open("test.txt", 'r')
# print(f.readline())

# f.close()
# f = open("test.txt", "w")
# f.write("I did not want to delete the content, but it got deleted.")
# f.close()
# open("onefile.txt", "a")
# # open("myfile.txt", "x")
# f = open("yourfile.txt", "w")
