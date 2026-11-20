from string import ascii_letters, digits, punctuation

# for i in digits:
#     for j in digits:
#         for k in digits:
#             for l in digits:
#                 print(i, j, k, l)

for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
                print(i, j, k)


for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
             print(i, j, k)