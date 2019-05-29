import json
import csv
import xml.dom.minidom

##all the information will be store in a touple list: [(firstName, monthly_salary)]

##get information from json
json_records = []
with open('week-04\day-03\employees.json', 'r') as jsonr:
    json_dict = json.loads(jsonr.read())
##store into the json records
for dict in json_dict:
    json_records.append((dict['name'].spilt('')[0], dict['monthly_salary']))

##get the information from csv
csv_records = []
with open('week-04\day-03\employees.csv') as csvr:
    head = csvr.readline()
    head = head.split(',')
    head[5] = head[5][:-1]
    lines = csvr.readlines()
    csvr_list = []
    for line in lines:
        line = line.split(',')
        line[5] = line[5][:-1]
        csvr_list.append(line)

for record in csvr_list:
    firstName = record[1]
    salary_by_month = record[-1]
    csv_records.append((firstName, salary_by_month))

##Get the information from xml
xml_records = []
xmlr = xml.dom.minidom.parse('week-04\day-03\employees.xml')
root = xmlr.documentElement
records = root.getElementsByTagName('record')

for record in records:
    firstName = record.getElementsByTagName('name').split('')[0]
    salary_by_month = str(int(record.getElementsByTagName('salary_by_year'))/12)
    xml_records.append((firstName, salary_by_month))