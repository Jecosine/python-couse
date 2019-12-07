import os
import re
# Use regular expression to get image which is before process (filter images' names end with '_w', '_s'...)
ban_ext = ['_w', '_s', '_640']
pattern = ''
for i in ban_ext:
    pattern += "(?:{0})".format(i.strip()) + '|'
pattern = pattern[:-1]
def get_imlist(path, ext):
    global pattern
    pattern += ext
    # print pattern
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext) and not re.search(pattern, f)]
