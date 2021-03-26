def unli():
    
    matn = input('Matn kiriting: ')
    matn = matn.lower()
    if matn.count('a') or matn.count('e') or matn.count('i') or matn.count('o') or matn.count('u') or matn.count("o'"):
        soni = matn.count('a') + matn.count('e') + matn.count('i') + matn.count('o') + matn.count('u') + matn.count("o'")
    print(soni)
unli()