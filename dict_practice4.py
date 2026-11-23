words = ["model", "data", "python", "data","model", "analysis", "data"]
new_list= []
new_dict = {}
for word in words:
    new_dict[word] = new_dict.get(word, 0) +1
    if new_dict[word] > 1:
        if word not in new_list:
            new_list.append(word)

print("Frequency:" , new_dict)
print("Repeated values:", new_list)