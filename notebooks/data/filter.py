import csv
from collections import Counter

usernames = []
with open('data/filter2.csv') as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
        usernames.append(row[0])

with open('data/training.csv') as csvfile:
    file_reader = csv.reader(csvfile)
    with open('data/final.csv', 'a',newline='') as csvfile1:
        for row in file_reader:
                spamwriter = csv.writer(csvfile1)
                if row[4] in usernames:
                    spamwriter.writerow(row)

# counter = {}
# with open('data/training.csv') as csvfile:
#     file_reader = csv.reader(csvfile)
#     for row in file_reader:
#             usernames.append(row[4])

# counter = Counter(usernames).most_common()[300:400]
# # print(counter)
# with open('data/filter2.csv', 'a',newline='') as csvfile1:
#     spamwriter = csv.writer(csvfile1)
#     for i in counter:
#         spamwriter.writerow([i[0]])


