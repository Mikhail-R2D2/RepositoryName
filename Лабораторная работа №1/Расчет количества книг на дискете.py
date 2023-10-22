volume = 1509949.44 #Объём в байтах
pages = 100
string_ = 50
symbols = 25
one_symbol = 4
n = round(volume/(pages*string_*symbols*one_symbol),)

print("Количество книг, помещающихся на дискету:", n)
