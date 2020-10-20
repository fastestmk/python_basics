
word = 'geeks,for:geeks'
print(word.split(',')) # splitting at ','
print(':'.join(word.split(','))) # adding ':' in place of ','

s = 'aaa bbb ccc ddd'
# print(''.join(s.split())) # joining no-space where is space
print('_'.join(s.split())) # joinig
