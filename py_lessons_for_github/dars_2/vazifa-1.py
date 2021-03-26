""" №1 >> x ga kiritilgan ma'lumotlarni tekshirish """

x = input('x ga istalgan qiymatni kiriting >> ')
print('siz kiritgan ma\'lumot tipi: ', type(x))
print('kiritilgan ma\'lumot faqat raqamdan iboratligini tekshirish >> ',x.isdigit())
print('kiritilgan ma\'lumot faqat harflardan iboratligini tekshirish >> ', x.isalpha())
print('kiritilgan ma\'lumot faqat kichik harflardan iboratligini tekshirish >> ', x.islower())
print('kiritilgan ma\'lumot faqat katta harflardan iboratligini tekshirish >> ', x.isupper())

