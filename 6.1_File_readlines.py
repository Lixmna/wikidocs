f=open(r'C:\Users\Lixmna\AppData\Local\Programs\Python\Python39\NEWS.txt','rt',encoding='UTF8')
lines = f.readlines()
import sys
sys.stdout.writelines(lines[-5:])
