def is_palindrome_iterative(word):
    if word == "":
        return False

    if word == word[::-1]:
        return True
    else:
        return False
