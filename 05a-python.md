# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are ordered sequences and have an index.
Lists are dynamic (modifiable) sequence of items while tuples are static sequence of items.

Tuples will work as keys in dictionaries, while lists won't because lists do not have a valid 'hash' method.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets can contain many elements. Lists are ordered sequences, while sets are unordered.
A list can have repeated values, while sets cannot.

Finding an element in a set (or a 'key' in a dictionary) is very fast because it uses hash values, while finding an element in a list requires you to traverse the list. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` are anonymous functions restricted to a single expression. They can be used wherever a function object is required. Also, they can access variables within the current/containing scope.

Ex.1
>>> g = lambda x: x**2
>>> print g(2)
4

Ex.2
>>> print map(lambda w: len(w), 'It is raining cats and dogs'.split())
[2, 2, 7, 4, 3, 4]

Ex.3
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool to transform one list into another list.
It is similar to using a filter and then a map in functional programming

Ex.1
>>> numbers =  [1,2,3,4,5,6]
>>> doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))

is equivalent to:
>>> doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

Any foor loop can b

Ex.2 Set comprehensions
>>> names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
>>> { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }

Ex.3 Dictionary comprehensions
>>> mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
>>> { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> from datetime import datetime
date_format = "%m-%d-%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print(delta.days)



b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> from datetime import datetime
date_format = "%d-%b-%Y"
a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)
delta = b - a
print(delta.days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





