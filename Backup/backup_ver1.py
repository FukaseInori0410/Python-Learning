import os
import time

# 要求：
# 需要备份的文件与目录应在一份列表中予以指定。
# 备份必须存储在一个主备份目录中。
# 备份文件将打包压缩成 zip 文件。
# zip 压缩文件的文件名由当前日期与时间构成。
# 我们使用在任何 GNU/Linux 或 Unix 发行版中都会默认提供的标准 zip 命令进行打包。
# 在这里你需要了解到只要有命令行界面，你就可以使用任何需要用到的压缩或归档命令。

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

# 使用zip命令打包
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 执行程序
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
