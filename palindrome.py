class Palindrome:
    # Méthode de classe testant si une chaine de Caracteres s est un palindrome
    def estPalindrome(s):
        # Une chaine d'un seul caractere ou une chaine vide sont des Palindromes
        if len(s) <= 1:
            return True
        # Si les premiers et derniers caracteres sont identiques
        # et si la sous-chaine restante est elle-meme
        # un palindrome, alors la chaine entiere est un palindrome
