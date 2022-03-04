y={'carl':40,'alan':2,'bob':1,'danny':3}
l=list(y.items())
dict=dict(l)
print("dictionary",dict)
l.sort()
print('ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('descending order is',l)
