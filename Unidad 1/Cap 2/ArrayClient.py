import Array

maxSize = 10
arr = Array.Array(maxSize)

arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting for 0 returns", arr.search(0))

print("Deleting for 17 returns", arr.search(17))

print("Setting item at index 3 to 33", arr.search(12))
arr.traverse()

