selling_books = int(input())
book_names = [input() for i in range(selling_books)]

best_seller = {}
for i in book_names:
    if i not in best_seller:
        best_seller[i] = 1
    else:
        best_seller[i] += 1

best_seller1 = dict(sorted(best_seller.items()))

sell_num = 0
book = ''
for i, j in best_seller1.items():
    if j > sell_num:
        book, sell_num = i, j
print(book)


