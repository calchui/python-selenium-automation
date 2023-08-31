# ****************  Level 1 ***********************
#           Task 1
def reverse_order(n: int):

    string = str(n)

    if string[0] == '-':

        return ('-' + string[:0:-1])

    else:

        return string[::-1]

print(reverse_order(-123))
print(reverse_order(456))


# #         Task 2
def are_anagrams(s1= str, s2= str):

    if len(s1) != len(s2):

        return False

    if sorted(s1.lower()) == sorted(s2.lower()):

        return True

    else:

        return False

print(are_anagrams('race', 'care'))
print(are_anagrams('hEArt', 'earth'))
print(are_anagrams('rattle', 'battle'))


# ****************  Level 2 ***********************
#           Task 3
def reverse_words(sentence: str):

    words = sentence.split()

    reverse_list = []

    for word in words:

        reverse_list.append(word[::-1])

    x = " ".join(reverse_list)

    print(x)

reverse_words("Hello World")
reverse_words("mistertwister")
reverse_words("Python is awesome")


#           Task 4 (THIS IS INCOMPLETE)
def repeat_digits(s: str):

    result = ""

    for char in s:

        result = char * s


    return result


print(repeat_digits(5))


#           Task 5
def shortcut(word: str):

    vowels = 'aeiou'

    result = ""

    for char in word:

        if char not in vowels:

            result = result + char

    return result


print(shortcut('hello'))
print(shortcut('goodbye'))







