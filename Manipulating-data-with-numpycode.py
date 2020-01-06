# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)

census = np.concatenate([new_record,data])
print(census)


# --------------
#Code starts here
age = census[:,[0]]
print(age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print("Maximum age is", max_age)
print("Minimum age is", min_age)
print("Mean age is", age_mean)
print("The standard deviation of the age is", age_std)
print("Looking at the data we can say that the country is Young Country")



# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
a = min(len_0,len_1,len_2,len_3,len_4)
if (a==len_0):
    minority_race=0
if(a==len_1):
    minority_race=1
if(a==len_2):
    minority_race=2
if(a==len_3):
    minority_race=3
else:
    minority_race=4
print("Index of the race having the least no. of citizens", minority_race)


# --------------
#Code starts here
import numpy as np
senior_citizens = np.array(census[census[:,0] >60])
working_hours_sum = senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print("The average working hours of senior citizens is", avg_working_hours)


# --------------
#Code starts here
import numpy as np
high = np.array(census[census[:,1]>10])
low = census[(census[:,1]<10) | (census[:,1]==10)]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]



