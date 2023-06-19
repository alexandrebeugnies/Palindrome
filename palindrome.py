class Palindrome:
    def __init__(self,chaine):
        self.chaine = chaine

    def __del__(self):
        print(self.chaine.upper())

    def test(self):
        return Palindrome.estPalindrome(self.chaine)
    # Méthode de classe testant si une chaine de Caracteres s est un palindrome
    def estPalindrome(s):
        # Une chaine d'un seul caractere ou une chaine vide sont des Palindromes
        if len(s) <= 1:
            return True
        # Si les premiers et derniers caracteres sont identiques
        # et si la sous-chaine restante est elle-meme
        # un palindrome, alors la chaine entiere est un palindrome

        # l´utilisation de l´indice -1 permet de recupere le dernier caractere d'une chaine
        # l'utilisation du caractere ':' permet d'extraire une sous-chaine en precisant les indices de debut et de fin.
        return s[0] == s[-1] and Palindrome.estPalindrome(s[1:-1])

        
