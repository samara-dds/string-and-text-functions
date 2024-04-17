# string-and-text-functions

## 🚀 Vowel Count

### 📋 Description:

Write a function in Python called count_vowels that takes a string as input and returns the number of vowels present in that string. Consider that the vowels are 'a', 'e', ​​'i', 'o' and 'u' (lowercase and uppercase).

First, define the count_vowels function that accepts a string as an input argument.

```
 def tell_vowels(string):

```

Initialize a variable to store the number of vowels found in the string. You can start with 0.

```
def tell_vowels(string):
    counter_vowels = 0
```

Use a loop to loop through each character in the input string.

```
def tell_vowels(string):
    counter_vowels = 0
    for caracter in string:
```

For each character in the string, check whether it is a vowel. You can do this by comparing the character with a list of vowels ('a', 'e', ​​'i', 'o', 'u') in lowercase and uppercase.

```
def tell_vowels(string):
    counter_vowels = 0
    for caracter in string:
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
```

If the current character is a vowel, increment the vowel counter.

```
def tell_vowels(string):
    counter_vowels = 0
    for caracter in string:
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
            counter_vowels += 1
```

After traversing the entire string, return the counter value, which represents the total number of vowels found in the string.

```
def tell_vowels(string):
    counter_vowels = 0
    for caracter in string:
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
            counter_vowels += 1
    return counter_vowels

print(tell_vowels("Hello World")) # Exit: 3
```

## Invert a String

### Description:

Write a function in Python called invert_string that takes a string as input and returns that string inverted.

First, define the invert_string function that accepts a string as an input argument.

```
def reverse_string(string):

```

Initialize a variable to store the reversed string. You can start with an empty string.

```
 string_reverse= ""
```

Use a loop to cycle through each character in the input string, from last to first.

```
 for item in range(len(string) - 1, -1, -1):
```

For each character in the input string, add it to the inverted string you are constructing.

```
string_reverse += string[item]
```

After traversing the entire string, return the inverted string you constructed.

```
return string_reverse
```

to finish:

```
string_original = "Hello World"
string_reverse= reverse_string(string_original)
print(string_reverse)  # Exit: "dlroW olleH"
```

with ❤️ per Samara
