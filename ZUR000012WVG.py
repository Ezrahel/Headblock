class PalindromeChecker:
    def __init__(self, mypali):
        self.mypali = mypali

    def pali_non_pali(self):
        # Split the parameter by spaces and initialize empty lists for results
        items = self.mypali.split()
        palindrome_results = []
        non_palindrome_results = []
        
        for i in items:
            # Check if the item is a palindrome
            if i == i[::-1]:
                # If it's a palindrome, add it to the palindrome results with a label
                palindrome_results.append(f"{i[::-1]}")
            else:
                # If it's not a palindrome, add it to the non-palindrome results with a label
                non_palindrome_results.append(f"{i[::-1]} ")
        
        return {"palindromes": palindrome_results, "\n non_palindromes": non_palindrome_results}


#I tried out mixture of Palindrome and non Palindrome 
params = "abcd5dcba 1230321 0124210 hello world"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()


print(f"\n{results} ")

params = "ada"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()

print(results)

params = "Israel Xyluz"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()

print(results)

params = "Ande Emmanuel"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()

print(results)


params = "Seyi Onifade"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()

print(results)


params = "Am tired"
finder = PalindromeChecker(params)
results = finder.pali_non_pali()

print(results)
