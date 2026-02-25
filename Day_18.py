# --------------------------String Problem------------------------ #

# Reverse a string without using extra space
def reverse_string(s):
    print("-----Reverse String------")
    s = list(s)
    left,right = 0,len(s)-1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return " ".join(s)
result = reverse_string("New")
print(result)
# Check if a string is a palindrome
def is_palindrome_string(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
result = is_palindrome_string("level")
print(result)
# Find the first non-repeating character in a string
def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
result = first_non_repeating_char("hello")
print(result)
# Count the frequency of each character in a string
def character_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return freq
print(character_frequency("hello"))
# Check if two strings are anagrams
def are_anagram(s1,s2):
    return sorted(s1.lower()) == sorted(s1.lower())
print(are_anagram("listen","silent"))

# Basic String Compression
def string_compression(s):
    if not s:
        return s
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s
print(string_compression("aabbccc"))

# Find longest common prefix among a set of strings
def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
print(longest_common_prefix(["flower", "flow", "flight"]))


    




