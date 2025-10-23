input_string=input("Enter a string:")
char_freequency={}
for char in input_string:
    char_freequency[char]=char_freequency.get(char,0)+1
print(f"character freequencies in'{input_string}':")
for char,count in char_freequency.items():
    print(f"{char} occurs {count} times.")
