'''filter: pass each element in iterable and return only the once that evaluate to true'''
#wap to return even values in the below list
# l = [1,2,3,4,5,6]
# def even(num):
#     if num % 2 == 0:
#         return num
#
# res = filter(even, l)
# print(list(res))

# ev = lambda item: item % 2 ==0
# re = filter(ev, l)
# print(list(re))

#wap that returns a list of strings with odd length
# l = ['hi', 'how', 'are']
# def odd_str(word):
#     if len(word) % 2 != 0:
#         return word
#
# res = filter(odd_str, l)
# print(list(res))

# od = lambda item:len(item) % 2 !=0
# res = filter(od, l)
# print(list(res))


#wap which returns all the words starting with vowels
# l = "hell how are you"
# l1 = l.split()
# def vowel_(word):
#     if word[0] in 'aeiouAEIOU':
#         return word
# res = (filter(vowel_, l1))
# print(list(res))

# e = lambda item: item[0] in 'aeiouAEIOU'
# res = filter(e, l1)
# print(list(res))


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def sqr(num):
#     if num % 2 == 0:
#         return num ** 2
# res = (filter(sqr, l))
# print(list(res))


