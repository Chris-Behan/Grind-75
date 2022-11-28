from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    """
    Approach: Create a dictionary of character counts for each string then compare the contents
    of these counts, confirming that the dictionaries are the same length and that their values
    are the same.

    Time Complexity: O(n + m)
    We loop through each string to build up the count dictionaries then loop through one of the
    count dictionaries, comparing its contents with the other. n + n + max(n,m) = O(n + m).

    Space Complexity: O(n + m)
    Input strings are length n and m respectively. We then create two dictionaries of length n and
    m.

    Auxiliary space: O(n + m)
    We create two dictionaries that in the worse case have the name number of keys as the input
    strings if all the characters in those input strings are unique.

    Args:
        s (str): first input
        t (str): second input

    Returns:
        bool: whether or not the string is an anagram.
    """
    s_char_counts: dict[str, int] = defaultdict(int)
    for c in s:
        s_char_counts[c] += 1
    t_char_counts: dict[str, int] = defaultdict(int)
    for c in t:
        t_char_counts[c] += 1
    if len(s_char_counts) != len(t_char_counts):
        return False
    for char, count in s_char_counts.items():
        if t_char_counts[char] != count:
            return False
    return True


s = "anagram"
t = "nagaramm"
print(isAnagram(s, t))
