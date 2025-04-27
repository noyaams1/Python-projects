def longest_word(words):
        if not words:
                return None
        max_length = max(words, key=len)
        return (max_length,len(max_length))

print(longest_word(["apple", "banana", "kiwi", "orange"]))
print(longest_word(["cat", "dog", "elephant", "mouse"]))
print(longest_word([]))
print(longest_word(["a", "bb", "ccc", "dddd"]))
