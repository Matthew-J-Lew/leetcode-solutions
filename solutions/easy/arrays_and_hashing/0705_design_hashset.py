"""
Problem: 705 - Design HashSet
Difficulty: Easy
Topic: Hashing / Data Structures

Approach:
- Use an array of buckets (lists) to handle collisions using separate chaining.
- Each key is hashed to an index using modulo division.
- For `add`, insert into the bucket if not already present.
- For `remove`, delete from the bucket if it exists.
- For `contains`, check if the key is in its corresponding bucket.

Time Complexity: O(1) average per operation, O(n) worst case if many collisions
Space Complexity: O(n) for storing up to n keys
"""

class MyHashSet:

    def __init__(self):
        # Initialize buckets
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Simple hash function to map a key to a bucket index
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        # Only add if key doesn't already exist
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]
        return key in bucket
