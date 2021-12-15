import os
import time

# 新增条件：
# 使用时间作为文件名，存储在以当前日期为名字的文件夹中

# 待备份文件目录存在一个列表中
source = ['D:\\codes\\Python\\PythonLearning']

# 备份文件存在一个字符串中且必须是主目录
target_dir = 'D:\\Backup'

# zip 压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep +\
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
