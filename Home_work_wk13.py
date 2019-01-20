import csv
with open('long_service.csv')as a:
    csv_f = csv.reader(a)
    staff_emails = []

    for row in csv_f:
        staff_emails.append(row[2])

with open('new_list.csv') as b:
    csv_f = csv.reader(b)
    new_staff_emails = []

    for row in csv_f:
        new_staff_emails.append(row[2])

staff_emails = set(staff_emails)
new_staff_emails = set(new_staff_emails)
new_staff = staff_emails.difference(new_staff_emails)

print (new_staff)