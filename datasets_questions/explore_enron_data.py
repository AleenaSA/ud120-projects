#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sklearn

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
print(len(list(enron_data.values())[0]))

count=0

for user in enron_data:
	if(enron_data[user]["poi"]==1):
		count=count+1

print(count)

#poi_names=open("../final_project/poi_names.txt",'r')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("../final_project/poi_names.txt")-2)
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

most_paid=""
highest_payment=0;

for key in ('LAY KENNETH L',"SKILLING JEFFREY K", 'FASTOW ANDREW S'):
	if enron_data[key]["total_payments"] >highest_payment:
		highest_payment=enron_data[key]["total_payments"]
		most_paid=key
print(most_paid)
print(highest_payment)

count_salary = 0
count_email = 0
count_total_payments=0
total_count=0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
    if enron_data[key]['total_payments'] != 'NaN':
    	count_total_payments+=1
    total_count+=1
print (count_salary)
print (count_email)
print (count_total_payments)
print (count_total_payments/total_count*100)