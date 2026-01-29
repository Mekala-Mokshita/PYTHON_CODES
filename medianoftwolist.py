# Take input for first list
nums1 = list(map(int, input("Enter elements of first list: ").split()))

# Take input for second list
nums2 = list(map(int, input("Enter elements of second list: ").split()))

# Merge and sort
n = nums1 + nums2
n.sort()

# Find median
x = len(n) // 2

if len(n) % 2 == 0:
    median = (n[x - 1] + n[x]) / 2.0
else:
    median = float(n[x])

print("Median:", median)
