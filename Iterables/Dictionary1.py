x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

for key, value in x.items():
    if isinstance(value, (list, tuple, dict, set)):
        print(f'{key}:')
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f'  {sub_key}: {sub_value}')
        else:
            for item in value: # if we want to print index then, index,item in enumarate(value)
                if isinstance(item, tuple):
                    for i in item:
                        print(f'{i}')
                elif isinstance(item, dict):
                    for sub_key, sub_value in item.items():
                        print(f'  {sub_key}: {sub_value}')
                else:
                    print(f'  {item}')
    else:
        print(f'{key}: {value}')
