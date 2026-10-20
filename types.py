#10 tam ededdir, int
#10.0 kesrli ededdir, float
#"10" metn tipidir, string-str
#true bool ifadesidir, bool
# "True" metn tipidir, string-str
#3+2.0 float
#"3" + "2" string-str
#10/2 float olur, çünki / emeliyyatı həmişə float qaytarır. Eger // ile bölünerse int qaytarır.

print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type("True"))
print(type(3+2.0))
print(type("3" + "2"))
print(type(10/2))

print(type(10//2))