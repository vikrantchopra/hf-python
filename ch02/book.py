book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)

#print(booklist)

print(booklist[0:3])

plist = ''.join(booklist[0:3])

print(plist)

plist = ''.join(booklist[-6:])
print(plist)


print(''.join(booklist[4:14]))

print(''.join(booklist[13:3:-1]))

backwards = booklist[::-1]
print(''.join(backwards))
