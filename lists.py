
# List is the ordered collection of elements.
# Lists is used to represent group of elements in ordered way with dynamic nature.
# Lists are ordered, mutable, and allow duplicate values.
emptyList=[]
print(len(emptyList))
language =["js","python","java","c++","c"]
print(language[3])  # indexing
print(language[4])
print(language[-1])  # negative indexing
# Slicing:
print(language[0:2])  # from index 1 to index 2 
print(language[2:0])   # from index 2 to index 0  , we get empty list as output because slicing works from left to right
print(language[4:1])   # from index 4 to index 1 , we get empty list as output because slicing works from left to right
print(language[1:])   # from index 1 to end
print(language[:3])   # from start to index 3
print(language[:])    # from start to end
print(language[4:1:-1])  # reverse slicing from index 4 to index 1, we get ['c', 'c++', 'java'] as output because of step -1
print(language[1:4:-1])  # reverse slicing from index 1 to index 4, we get empty list as output because slicing works from left to right
print(language[::-1])  # reverse the list, we get reversed list as output because of step -1
print(language[3:4:-1])  # reverse slicing from index 3 to index 4, we get empty list as output because slicing works from left to right