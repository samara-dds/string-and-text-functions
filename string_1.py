
def tell_vowels(string):
    counter_vowels = 0
    for caracter in string:
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
            counter_vowels += 1
    return counter_vowels
print(tell_vowels("Hello World"))


def reverse_string(string):
    string_reverse= ""
    for item in range(len(string)-1, -1, -1):
        string_reverse += string[item]
    return string_reverse

string_original = "Hello World"
string_reverse= reverse_string(string_original)
print(string_reverse)