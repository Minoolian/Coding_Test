buger=[]
bever=[]
min=4000

for i in range(3):
    buger.append(int(input()))
for i in range(2):
    bever.append(int(input()))
for i in buger:
    for j in bever:
        if min>(i+j):
            min=i+j

print(min-50)