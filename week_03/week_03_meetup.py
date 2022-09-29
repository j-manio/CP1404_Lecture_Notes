"""
Files and Exception
"""

# FILENAME = "testfile.txt"
# in_file = open(FILENAME, "r")
# text = in_file.read()
# line_number = 0
# for line in in_file:
#     line_number += 1
# in_file.close()
# print(text)

# name = input('Name: ')
# out_file = open('testfile.txt', 'w')
#
# out_file.close()
# # print(name)
# # with
# with open('testfile.txt', 'w') as out_file:
#     print(name, file=out_file)

strings = ['Joco', 'Rob', 'Royce']
for string in strings:
    with open(f'files/{string}.txt', 'w') as out_file:
        print(string, file=out_file)
