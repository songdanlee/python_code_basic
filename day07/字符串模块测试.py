from str_function_mo import *

print(str_lower("ABCDEFcedff&&*1223"))
print(str_upper("ABCDEFcedff&&*1223"))

print("12CD3456ABCDCD".find("CD"))
print(str_find("12CD345CD6ABCDCD", "CD"))

print(str_rfind("123456ACabcd","bc"))
print("123456ACabcd".rfind("bc"))

print("1234123131".isdigit())
print(str_isdigit("1234111211112313213"))

tu = "1236789abcada".partition("abcada")
print(tu)
print(str_partition("1236789abcada","abcada"))

print("acd123456".startswith("acda"))
print(str_startswith("acd123456", "acda"))


print("acd1234567 ".endswith("567 "))
print(str_endswith("acd1234567 ","567 "))