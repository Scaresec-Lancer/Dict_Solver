# 定义字典处理函数，接受通过readlines方法读入的对象，输出去掉换行的列表
import os

 

def list_solve(f):
    ls=[]
    for i in f:
        if '\n' in i:
            ls.append(i[:-1])
        else:
            ls.append(i)
    print("\n成功处理"+str(len(ls))+"项\n")
    return ls

# 定义写入函数
def write_dict(a):
    with open('1.txt','a') as fp:
        fp.write(a+"\n")

def program_main():
    # 定义ci变量用来计数新增了多少
    ci=0       

    # 读取主字典，生成密码列表，方便查重
    with open('1.txt','r') as fp:
        f=fp.readlines()
        ls=list_solve(f)
        

    # 读取新字典，生成密码列表
    with open('2.txt','r') as fp2:
        g=fp2.readlines()
        ls2=list_solve(g)
        
    # 进行比较，主字典没有的写入
    for items in ls2:
        if items not in ls:
            write_dict(items)
            ci+=1
        else:
            pass
    print("新增"+str(ci)+"项")

program_main()
