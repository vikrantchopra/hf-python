phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


#for i in range(4):
#    plist.pop()
#plist.pop(0)
#plist.remove("'")
#plist.extend([plist.pop(), plist.pop()])
#plist.insert(2, plist.pop(3))
#new_phrase = ''.join(plist)

new_phrase = plist[1:3] + plist[5:6] + plist[4:5] + plist[-5:-7:-1]
new_phrase = ''.join(new_phrase)
print(plist)
print(new_phrase)
