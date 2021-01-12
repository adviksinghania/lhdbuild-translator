# !/bin/python3
# translator.py
# Author : Advik Singhania
# Date: 12th January, 2021
# NOTE: Requires internet connection. see README.md for more information.
'''A Python script that translates a word using GoogleTrans API'''

try:  # Check and import if the module for translation is installed or not
    import googletrans
except ModuleNotFoundError:
    print('GoogleTrans package is not installed.')
    print("Run 'python -m pip install googletrans==4.0.0-rc1' on your terminal to install it.")
    exit()

# Initializatio phase:
# The text to be translated as a string input
text = input('Enter the text you want to be translated: ')
# The destination language
tolang = input('Enter the language you want the text to be translated: ')
tolang = tolang.lower()  # Converting it to lowercase
# Getting the languages available as a dictionary
# With the language as the key and language code as the value
langs = googletrans.LANGCODES

# Processing phase:
if tolang in langs.keys():  # If the language is in the keys of LANGCODES
    tr = googletrans.Translator()  # Making an instance of the translator
    # The converted language using the value from the 'langs' dictionary
    out = tr.translate(text, dest=langs[tolang])
    print('Translated text:', out.text)  # Printing the language as a text
else:
    print('Support for', tolang, 'not available.')
