from collections import Counter

f = open(r"singular.txt", encoding='utf-8')

data = f.readlines()
data = [i[:-1] for i in data if len(i) == 6]

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i])
print(counter)

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i][0])
print(counter)

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i][1])
print(counter)

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i][2])
print(counter)

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i][3])
print(counter)

counter = Counter()
for i in range(len(data)):
    counter += Counter(data[i][4])
print(counter)


