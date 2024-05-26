import function as ff
from fake_math import divide as fake_d
from true_math import divide as true_d

ff.greeting_1()
ff.greeting_2()
print(__name__)

result1 = fake_d(69, 3)
result2 = fake_d(3, 0)
result3 = true_d(49, 7)
result4 = true_d(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)