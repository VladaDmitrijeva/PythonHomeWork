months = [{"january" : 2, "december" : 3, "february" : 4},
{"january" : 1, "december" : 1, "february" : 4},
{"january" : 5, "december" : 3, "february" : 2},]

# def sumofkey(dic):
#     total = 0
#     for i in dic.values():
#         total = sum(dic)
#     return total

# print(sumofkey(months))

result = {}
for dics in months:
    for i in dics.keys():
        result[i] = sum(i)

print(str(result))
    