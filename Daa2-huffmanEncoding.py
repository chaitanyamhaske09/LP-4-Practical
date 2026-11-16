import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

def printCodes(root, code):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.ch, ":", code)
        return

    printCodes(root.left, code + "0")
    printCodes(root.right, code + "1")

n = int(input("Enter number of characters: "))

pq = []

for i in range(n):
    ch, freq = input("Enter character and frequency: ").split()
    heapq.heappush(pq, (int(freq), i, Node(ch, int(freq))))

while len(pq) > 1:
    left = heapq.heappop(pq)[2]
    right = heapq.heappop(pq)[2]

    newNode = Node('\0', left.freq + right.freq)
    newNode.left = left
    newNode.right = right

    heapq.heappush(pq, (newNode.freq, n, newNode))
    n += 1

print("Huffman Codes:")
if pq:
    printCodes(pq[0][2], "")
    
#     1. Greedy Method – Short Explanation
# The Greedy Method is an algorithmic technique that makes the best possible choice at each step to get an optimal solution.
# - It selects the best available option.
# - It makes decisions step by step.
# - It does not reconsider previous choices.
# Example: Huffman Encoding uses the Greedy Method by repeatedly selecting the two characters with the lowest frequencies.
# 2. Huffman Encoding – Short Explanation
# Huffman Encoding is a Greedy Algorithm used for lossless data compression.
# - It assigns shorter binary codes to frequently occurring characters.
# - It assigns longer binary codes to less frequently occurring characters.
# - It uses a Min Heap to select minimum frequencies.
# - Left branch represents 0 and right branch represents 1.
# Example:
# For input AABBBC:
# Character	Frequency	Huffman Code
# A	2	10
# B	3	0
# C	1	11


# 3. Time and Space Complexity
# Let n = number of unique characters.
# Complexity	Value	Explanation
# Time Complexity	O(n log n)	Building and processing the Min Heap
# Space Complexity	O(n)	Storing frequency, heap, tree and codes