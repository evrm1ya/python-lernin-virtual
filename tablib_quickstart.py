import tablib
import random

data = tablib.Dataset()

names = ['Steph Curry', 'Michael Jordan']

for name in names:
    fname, lname = name.split()
    data.append([fname, lname])

data.headers = ['First Name', 'Last name']

data.append_col([22, 20], header='Age')

ages = data['Age']
print float(sum(ages)) / len(ages)

# view the dataset
print data.dict

# dynamic columns
def random_grade(row):
    return (random.randint(60, 100) / 100.0)

data.append_col(random_grade, header='Grade')

print data.yaml

del data['Grade']

print data.yaml

# first arg passed to callable is current row
def guess_team(row):
    lname = row[1]

    if lname == 'Jordan':
        return 'Bulls'
    elif lname == 'Curry':
        return 'Warriors'
    else:
        return 'Who cares'

data.append_col(guess_team, header='Team')

print data.yaml

# Filtering with tags
players = tablib.Dataset()

players.headers = ['first', 'last', 'team']

players.rpush(
        ['Steph', 'Curry', 'Warriors'], 
        tags=['west']
        )
players.rpush(
        ['Lebron', 'James', 'Cavs'], 
        tags=['east']
        )
players.rpush(
        ['Michael', 'Jordan', 'Bulls'], 
        tags=['retired', 'east']
        )

print players.filter(['retired']).yaml
print players.filter(['east']).yaml

# Separators
daniel_tests = [
        ('11/24/09', 'Math 101 Mid-term Exam', 56.),
        ('05/24/10', 'Math 101 Final Exam', 62.)
        ]

suzie_tests = [
        ('11/24/09', 'Math 101 Mid-term Exam', 56.),
        ('05/24/10', 'Math 101 Final Exam', 62.)
        ]

tests = tablib.Dataset()
tests.headers = ['Date', 'Test Name', 'Grade']

tests.append_separator("Daniel's Scores")

for test_row in daniel_tests:
    tests.append(test_row)

tests.append_separator("Susie's Scores")

for test_row in suzie_tests:
    tests.append(test_row)

with open('dist/grades.xlsx', 'wb') as f:
    f.write(tests.xlsx)
