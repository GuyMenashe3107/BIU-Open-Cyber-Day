# BIU crypto open-day 2020 12/11/2020
# my solutions...

def break_pubkey(g, p, y):
    A = dict()
    rev_A = dict()
    step = (g ** 1000000) % p
    # step = 6165167147278298
    print(step)
    tmp = step % p
    for i in range(1, 10**6):
        A[i] = tmp
        rev_A[tmp] = i
        if y == A[i]:
            return 1000000*i
        tmp = (tmp * step) % p
    print("done creating arrays...")
    tmp = (y) % p
    for j in range(1, 10**6):
        tmp = (tmp * g) % p
        i = rev_A.get(tmp)
        if i is not None:
            return 1000000 * i - j


def decrypt(s, keyA, keyB):
    sl = ""
    s1 = ""
    s2 = ""
    for i in s:
        sl += chr((ord(i) - ord('a') - 13) % 26 + ord('a'))

    for i in range(0, len(sl)):
        if i % 2 == 0:
            s1 += chr((ord(sl[i]) - ord(keyA)) % 26 + ord('a'))
        else:
            s2 += chr((ord(sl[i]) - ord(keyB)) % 26 + ord('a'))
    return s1, s2


print("...p1s1...")

s = "qcvffunoqbiwnnaoghnwtcrb"
s1, s2 = decrypt(s, 'a', 'b')

print("Alice:", s1, "Bob:", s2)

s = "oblshukjxgbjhdyjablmymzzvvkbpqjqafpbvsubhoydff"

print("...p1s2...")


for key in "abcdefghigklmnopqrstuvwxyz":
    # print("key is: ", key)
    s1, s2 = decrypt(s, key, key)
    # print(s1, s2)

# allis key is u!!!!
# bob key is o!!!

print("Alice: ", decrypt(s, 'u', 'o')[0])
print("Bob: ", decrypt(s, 'u', 'o')[1])

print("...p2...")
g = 123456789
p = 11333555557777777
y = 610777178490757
print("x is ", break_pubkey(g, p, y))

g = 123456789
p = 11333555557777777
y = 1787092149484102
print("Guy's x is ", break_pubkey(g, p, y))
