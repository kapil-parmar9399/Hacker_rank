# Collections.OrderedDict()

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Collections.OrderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem)

## Problem Description

### [collections.OrderedDict](https://docs.python.org/2/library/collections.html#ordereddict-objects)

An *OrderedDict* is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

**Example**

**Code**

```
>>> from collections import OrderedDict
>>>
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>>
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>>
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>>
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

```

**Task**

You are the manager of a supermarket. **
You have a list of  items together with their prices that consumers bought on a particular day.

Your task is to print each `item_name` and `net_price` in order of its first occurrence.

`item_name` = Name of the item.

`net_price` = Quantity of the item sold multiplied by the price of each item.

Input Format**

The first line contains the number of items, . **
The next  lines contains the item's name and price, separated by a space.

Constraints**

**Output Format**

Print the `item_name` and `net_price` in order of its first occurrence.

**Sample Input**

```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

```

**Sample Output**

```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

```

**Explanation**

*BANANA FRIES*: Quantity bought: , Price:

`Net Price`:

*POTATO CHIPS*: Quantity bought: , Price:

`Net Price`:

*APPLE JUICE*: Quantity bought: , Price:

`Net Price`:

*CANDY*: Quantity bought: , Price:

`Net Price`:

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Collections.OrderedDict()
# Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Difficulty: Easy
# Language: python3

n = int(input())

items = {}

for i in range(n):
    data = input().split()

    name = " ".join(data[:-1])
    price = int(data[-1])

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
