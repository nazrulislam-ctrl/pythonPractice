info={"name": "Karim", "age": 25, "eligible": True }
# print(info.keys())
# print(info.values())
# print(info.get("name"))
# print(info["age"])

# for i in info.keys():
#     print(f"The value corresponding to the key {i} is {info[i]}")

# print(info.items())
# for key, value in info.items():
#     print(f"The corresponding value to the key {key} is {value}")

#2. *****Update Method******
ep1={122: 54, 123: 35, 532: 24, 632:52}
ep2={222: 62, 455: 90}
# ep1.update(ep2)
# ep1.clear()
# ***pop any particular key and value from the dictionary***
# ep1.pop(122)
# ***pop the last item of the dictionary*** 
# ep1.popitem()
# ***to delete the dictionary***
# del ep1
del ep1[122]
print(ep1)