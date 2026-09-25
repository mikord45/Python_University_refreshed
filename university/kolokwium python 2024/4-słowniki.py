d1 = {}
d1['zwierz'] = 'pies'
d1[78] = 514
print(d1)

d2 = {"klucz": "wartość", 123: 'abc', True: [1, 4, 6]}
print(d2)

d3 = dict()
d3["test"] ="test123"

keys = ['key0', 'key1', 'key2']
values = range(3)
zips = zip(keys, values)
print(zips)
list1 = list(zips)
print(list1)
dict1 = dict(zip(keys, values))
print(dict1)

dict2 = dict.fromkeys([1,2,3])
print(dict2)
dict3 = dict.fromkeys([1,2,3], 5)
print(dict3)

dict4 = {'a': 'valueA', 'b': 'valueB'}
print(dict4.get('a'))
print(dict4.get('b'))
print(dict4.get('c'))
print(dict4.get('c', 'brak'))

dict5 = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(len(dict5))
print('key2' in dict5)
print('key4' in dict5)
print(dict5.keys())
print(dict5.values())
print(dict5.items())

dict6 = {'python': 2.7, 97: 'a', 65: 'A'}
dict6['python'] = 3.0
print(dict6)
del dict6[97]
print(dict6)
dict6.pop('python')
print(dict6)
dict6.update({1:2, 3:56})
print(dict6)
dict6.update({'one':"xd", 65:10})
print(dict6)

# dict7 = {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
# print(dict7)
# dict7.pop()
# print(dict7)
