poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun
    use Python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')  # 去掉文件中每行包含的换行符，否则会空出一行，python输出会自动换行
f.close()
