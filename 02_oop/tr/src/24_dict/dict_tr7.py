keys_str = "key1,key2,key3"
values_str = "1,2,3"
keys = keys_str.split(",")
values = [int(v) for v in values_str.split(",")]
print({k: v for k, v in zip(keys, values)})
