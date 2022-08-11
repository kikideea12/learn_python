# Sets:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# * Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry",}

print(len(thisset))

set1 = {"apple", "banana", "cherry",}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry",}
print(type(myset))

thisset = set(("apple", "banana", "cherry",)) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry",}

for x in thisset: 
    print(x)

thisset = {"apple", "banana", "cherry",}

print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry",}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry",}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry",}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry",}

thisset.remove("banana")

print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry",}

thisset.discard("banana")

print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset 

thisset = {"apple2", "banana2", "cherry2"}

print(thisset)
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)