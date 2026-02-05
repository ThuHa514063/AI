# # a = (1, 2, 3, 4, 5)

# # for i in a:
# #     if i % 2 == 0:
# #         i = 1
# #     print(i)
    
# # b = [1, 2, 3, 4, 5]

# # for i in range(len(b)):
# #     if i % 2 == 0:
# #         b[i] = 0
# #     print(b[i])
    
# # c = {1, 2, 3, 4}

# # for i in c:
# #     print(i)

# d = {"name": "John", "age": 30, "score": 8}
# print(d)

# for k, v in d.items():
#     if k == "age":
#         d[k] = 18
#     if isinstance(v, int):
#         d[k] += 1

# print(d)
# kshjaljkhsdx

a = ["Hà", "Cảnh", "Ngọc", "Trường"]
print(a[2])
a.append("Đăng")
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
a.extend(["Cảnh", "Đăng"])
print(a)
a.remove("Cảnh")
print(a)