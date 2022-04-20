>>> example=set()
>>> example.add(42)
>>> example.add(False)
>>> example.add(3.14159)
>>> example.add("thorium")
>>> example
{False, 42, 3.14159, 'thorium'}
>>> #for sets the order does not matter
>>> example.add(42)
>>> example
{False, 42, 3.14159, 'thorium'}
>>> #sets do not contain duplicate elements
>>> len(example)
4
>>> example.remove(42)
>>> example
{False, 3.14159, 'thorium'}
>>> len(example)
3
>>> example.remove(50) #gives error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 50
>>> example.discard(50) #does not give error
>>> example
{False, 3.14159, 'thorium'}
>>> 


>>> example2=set([28, True, 2.71828, "Helium"])
>>> len(example2)
4
>>> example2.clear()
>>> len(example)
3


>>> # Integer 1-10
>>> odds = set([1,3,5,7,9])
>>> evens=set([2,4,6,8,10])
>>> primes=set([2,3,5,7])
>>> composites=set([4,6,8,9,10])
>>> odds.union(evens)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> evens.union(odds)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> odds
{1, 3, 5, 7, 9}
>>> evens
{2, 4, 6, 8, 10}
>>> odds.intersection(primes)
{3, 5, 7}
>>> primes.intersection(evens)
{2}
>>> evens.intersection(odds)
set()
>>> primes.union(composites)
{2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> 2 in primes
True
>>> 6 in odds
False
>>> 9 not in evens
True
>>> 

