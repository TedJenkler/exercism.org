def find_anagrams(word, candidates):
    arr = list(word.lower())
    anagram = []
    for words in candidates:
        candidate = list(words.lower())
        if arr == candidate:
            continue
        if sorted(arr) == sorted(candidate):
            anagram.append(words)
    return anagram