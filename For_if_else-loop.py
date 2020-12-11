A = [10, 20, 30, 40, 50]
key = 30

for value in A:
    if value == key:
        print("Element found")
        break
    else:
        continue
else:
    print("Element not found")
    