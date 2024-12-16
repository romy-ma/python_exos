word = input("Type a word: ")
bool = True
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        bool = False
        break

if bool:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")


