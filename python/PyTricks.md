
# "json.dumps()


```python
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
```


```python
my_mapping
```




    {'a': 23, 'b': 42, 'c': 12648430}




```python
import json
```


```python
print(json.dumps(my_mapping,indent=4,sort_keys=True))
```

    {
        "a": 23,
        "b": 42,
        "c": 12648430
    }



```python
import this

```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python
from collections import namedtuple
```


```python
Car = namedtuple('Car', 'color mileage')
```


```python
my_car = Car('red', 3812.4)
```


```python
my_car.color
```




    'red'




```python
my_car.mileage
```




    3812.4




```python
my_car
```




    Car(color='red', mileage=3812.4)




```python

```


```python

```
