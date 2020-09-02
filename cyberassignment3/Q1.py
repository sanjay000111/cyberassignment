def panagram(string1):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if char not in string1.lower():
            return (print("Not a Panagram string."))
    print("Panagram string.")

panagram("The quick brown fox jumps over th lazy dog.")
panagram("Hello there")