import json
list='{"name":"sathish","age":25}'
print(list)
print(type(list))

''' json to dictionary '''
ok=json.loads(list)
print(ok)
print(type(ok))

''' dic to json '''

p={"name":"sathish",'age':25}
k=json.dumps(p)
print(p)
print(type(p))

''' convert to json '''
t=('sathish')
print(type(t))
o=json.dumps(t)
print(o)
print(type(o))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))