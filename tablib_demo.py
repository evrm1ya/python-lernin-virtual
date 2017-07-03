import tablib

data = tablib.Dataset()

data.append(['A', 1])
data.append(['B', 2])
data.append(['C', 3])

with open('dist/test.csv', 'wb') as f:
    f.write(data.csv)

with open('dist/test.xls', 'wb') as f:
    f.write(data.xls)

sheet1 = tablib.Dataset()
sheet1.append(['A1', 1])
sheet1.append(['A2', 2])

sheet2 = tablib.Dataset()
sheet2.append(['B1', 1])
sheet2.append(['B2', 2])

book = tablib.Databook([sheet1, sheet2])

with open('dist/book.xlsx', 'wb') as f:
    f.write(book.xlsx)
