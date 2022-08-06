fh = open('mbox-short.txt')
print(fh)

for lh in fh:
    lx = lh.rstrip()
    lx = lx.upper()
    print(lx)