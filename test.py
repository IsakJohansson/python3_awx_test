import sys
print(sys.version)
domain = 'xn--land-4qa.com'

d = bytes(domain, 'idna')

print(d)
