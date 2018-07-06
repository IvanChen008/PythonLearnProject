print("Hello Python!!!")
e=set("adsgjajsdlgagjlkj'''k")
f=set("wqtglkajskldgjqiotkln")
g=f-e
#Pyhon控制流
"""三种基本的控制流：
    1、顺序结构
    2、条件分支结构
    3、循环结构"""
b="9"
if(b=="9"):
    print("abc")

#if
a,b=10,1
if(a>19):
    print(a)
    if(b<9):
        print(b)
elif(a>9 and a<=19):
    print("a>9 and a<=19")
else:
    print("随意输出！！！")
#while
a=0
while(a<10):
    print("Hello While interation!")
    a+=1
#for
#for:遍历列表
a = ["aa","afgag",1,"cdg"]
for i in a:
    print(i)
#for:常规循环
#for i in range(0,10)
for i in range(0,10):
    print(str(i)+"Hello A")
    #print("Hello A")
#中断结构
#break、continue
#break:全部直接退出，整个循环都中断
#continue:中断一次循环
for i in a:
    if(i == "aa"):
        break
    print(i)

#输出乘法口诀
for i in range(1,10):
    for j in range(1,i+1):  
        print(str(i)+"*"+str(j)+"="+str(i*j),end="  ")
    print()
print()
#逆向输出乘法口诀
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end="  ")
    print()
print()
