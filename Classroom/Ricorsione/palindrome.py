def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        # Verifico che la prima e l'ultima lettera della parola siano uguali
        return word[0] == word[-1] and palindrome(word[1:-1])


if __name__=="__main__":
    print(palindrome("kayak"))
