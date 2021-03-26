# # Topshiriq:

# # 5. 0 dan 150 gacha bo'lgan oraliqdagi barcha Fibonachchi sonlarini toping.

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

birinchi_son = 0
ikkinchi_son = 1
rezerv = 0

while birinchi_son < 10000:
    print(birinchi_son)
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

    # №1  0 = 0 + 1
    # №2  1 + 1 = 2
    # №3  1 + 2 = 3
    rezerv = birinchi_son + ikkinchi_son
    # 0 = 1
    # 1 = 1
    # 
    birinchi_son = ikkinchi_son
    # 1 = 0
    # 1 = 1
    # 
    ikkinchi_son = rezerv