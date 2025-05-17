import re

text = "abcdefghijklmnopqrstuvwxyz"
second_text = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
'''
print(text[0:3])
print(second_text[1:4])
print()

find_pattern = re.compile(r'abc')

matches = find_pattern.finditer(text)   # Shows all matches in the string in the form of an iterator
print(matches)  # OUTPUT: <callable_iterator object at 0x000002434D2EB7C0>
print(type(matches))  # OUTPUT: <class 're.Match'>
for match in matches:
    print(match)    # OUTPUT: <re.Match object; span=(0, 3), match='abc'>
print()


match_two = find_pattern.search(text)  # Shows the first match in a string type
print(match_two)  # OUTPUT: <re.Match object; span=(0, 3), match='abc'>
print(match_two.group())  # OUTPUT: abc
print(match_two.span())  # OUTPUT: (0, 3)
print(match_two.start())  # OUTPUT: 0
print(match_two.end())  # OUTPUT: 3
print(match_two.string)  # OUTPUT: abcdefghijklmnopqrstuvwxyz
print(match_two.lastgroup)  # OUTPUT: None
print()


match_three = find_pattern.findall(text)  # Shows all matches in the string in the form of a list
print(match_three)  # OUTPUT: ['abc']
for match in match_three:
    print(match)  # OUTPUT: abc