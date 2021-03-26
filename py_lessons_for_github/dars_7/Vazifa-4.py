# 4. Satr kiritishni so'rash va shu satrda ishtirok etgan elementlarni yangi listga alohida element sifatida kirg'izish.
# Bitta element faqat 1 marta kiritilishi kerak.
# Masalan:
# agar satr = "abbcccc44444446!@#$%+++" bo'lsa 
# list = "abc46!@#$+"

n = input(' ')
z = set()
for i in n:
    z.update(i)
print(z) 