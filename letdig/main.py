from args import text

def run(text: str) -> tuple[int, int]:
    digits = "0123456789"
    letters = "qwertyuiopasdfghjklñzxcvbnm"

    num_digits = 0
    num_letters = 0

    for i in text.lower():
        if i in digits:
            num_digits += 1
        elif i in letters:
            num_letters += 1

    return num_letters, num_digits

letras, digitos = run(text)
print(letras, digitos)



# num_letters = 0
 #   num_digits = 0
    
   #for char_str in text:
    #    match ord(char_str):
     #       case n if (65 <= n <= 90) or (97 <= n <= 122):
      #          num_letters += 1
       #     case n if 48 <= n <= 57:
        #        num_digits += 1
    
    #return num_letters, num_digits

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
