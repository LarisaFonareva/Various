h, a, b = int(input()), int(input()), int(input())
print(max(0, h - b - 1) // (a - b) + 1)

# x=0
# rez=0
# while x<h:
#     x=x+a
#     rez += 1
#     if x<h:
#         x-=b
#     else:
#         break
# print(rez)