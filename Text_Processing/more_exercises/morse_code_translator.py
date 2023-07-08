morse_code_text = input().split("|")

translated_message = ""

MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                   '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                   '--..': 'Z'}

for word in morse_code_text:
    for letter in word.split():
        if letter != " ":
            translated_message += MORSE_CODE_DICT[letter]
    translated_message += " "

print(translated_message)