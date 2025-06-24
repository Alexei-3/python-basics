def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def add_numbers(a, b):
    return a+b
def reverse_string(s):
    return s[::-1]
def word_count(text):
    return len(text.split())
def format_name(name):
    return name.strip().title()

print(celsius_to_fahrenheit(0))    # 32.0
print(add_numbers(3, 5))           # 8
print(reverse_string("hello"))     # "olleh"
print(word_count("Hi there world")) # 3
print(format_name("  aLeXeI  "))    # "Alexei"
