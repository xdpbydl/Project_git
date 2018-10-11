# -*- coding: utf-8 -*-
'''把存在问题的脚本保存，下次解决'''
import  shutil,os
print(sorted(os.listdir('E:/TEMP/S/Python3/')))
path = 'E:/TEMP/S/Python3/{}/'.format(input('请输入目标文件夹——：'))  #目标路径  E:/TEMP/S/Python3/9.资源/      0.有问题的/1.原创/7.自动化测试/8.network
print(sorted(os.listdir(path)))
file = input('输入需要保存的文件名：')  #目标文件
sct = 'snake.py'    # 源文件

shutil.copyfile(sct,path+file)
print(sorted(os.listdir(path)))