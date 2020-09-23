import mycollection.list as myls
import mycollection.dict as mydc

list1 = myls.same_value_list()
list2 = myls.random_value_list()
print(list1)
print(list2)

keys = ["key1", "key2", "key3"]
dict1 = mydc.same_value_dictionary(keys)
dict2 = mydc.random_value_dictionary(keys)
print(dict1)
print(dict2)
