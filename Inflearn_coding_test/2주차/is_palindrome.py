input = "abcba"


def is_palindrome(string):
    length = len(string)

    for i in range(length):
        if string[i] != string[length-1-i]:
            return False

    return True


print(is_palindrome(input))