# Problem 2
#
# Во множестве №3 найдите объекты которых нет во множестве №2
# Множество № 2:

farm_1 = {"dog", "cat", "mouse", "sheep"}

# Множество № 3:

farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

r = farm_2.difference(farm_1)
print(r)
