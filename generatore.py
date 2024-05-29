def mygenerator():
   print('First item')
   yield 10
   print('Second item')
   yield 20
   print('Last item')
   yield 30

gen = mygenerator()
next(gen)
next(gen)
next(gen)
