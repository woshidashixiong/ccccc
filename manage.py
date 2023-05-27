from collections import Counter
names = []
while True:
    input_name = input()
    if input_name == "end":
        break
    names.append(input_name)

c = Counter(names)
for index,tu in enumerate(c.most_common(),start=1):
    print(f"第{index}名{tu[0]}票数{tu[1]}")
    
