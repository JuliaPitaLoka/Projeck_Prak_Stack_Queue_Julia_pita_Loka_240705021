def cek_palindrome(kata):
    stack = []
    
    # push setiap karakter ke stack
    for char in kata:
        stack.append(char)
    
    # pop dari stack untuk buat kata terbalik
    balik = ""
    while stack:
        balik += stack.pop()
    
    # cek palindrome
    if kata == balik:
        return f"{kata} adalah Palindrome"
    else:
        return f"{kata} bukan Palindrome"

# Contoh input
kata = input("Masukkan kata: ")
print(cek_palindrome(kata))

