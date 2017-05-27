from hashtable import Hashtable

dict = Hashtable()
dict.add("add", "test1")
dict.add("key", "debug")
dict["set"] = "item"

for i in range(12):
    dict[i] = i
print(dict[1])
dict[1] = -1
print(dict[1])
