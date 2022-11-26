
def isPalindrome(s: str) -> bool:
    """
    Approach: first convert the string into a list of lowercase alphanumeric characters.
    Then compare this list with itself in reverse order. Since a palindrome is just a sequence
    of characters that are the same when read both forward and backward, if the two lists
    are identical, they are a palindrome.

    Time Complexity: O(n)
    We iterate through the input string to produce the list of lowercase alphanumeric characters (n 
    operations). We then reverse the list (another n operations). Then compare the contents of the
    two lists (another n operations). n + n + n = O(n).

    Space Complexity: O(n)
    Input size of the string is n, and we create list of potentially the same size. n + n = O(n).

    Auxiliary space: O(n)
    n extra space required in the worst case to create out list of lowercase alphanumeric 
    characters.

    Args:
        s (str): input string

    Returns:
        bool: whether or not the input string is a palindrome
    """
    s_list = lowercase_alphanumeric_list(s)
    return s_list == s_list[::-1]


def lowercase_alphanumeric_list(s: str) -> list[str]:
    """
    Returns a list of the alphanumeric characters in a string, converting all letters to lowercase.
    non-alphanumeric characters are omitted from the list.

    Args:
        s (str): input string

    Returns:
        list[str]: list of lowercase alphanumeric characters
    """
    res = []
    for c in s:
        if c.isalnum():
            res.append(c.lower())
    return res
