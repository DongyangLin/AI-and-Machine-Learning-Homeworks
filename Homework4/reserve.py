class Goods:
    def __init__(self, id,name, price):
        self.id = id
        self.name = name
        self.price = price
    def __str__(self):
        return f'编号：{self.id} 商品名称：{self.name} 价格: {self.price}'
class ShopManager:
    def __init__(self,path):
        self.path=path
        self.shopdic = self.readFileToDict()
    def readFileToDict(self):
        f=open(self.path,'r',encoding='utf-8')
        clist=f.readlines()
        f.close()  
        index=0
        shopdic={}
        while index < len(clist):
            ctlist=clist[index].replace('\n','').split('|')
            good=Goods(ctlist[0],ctlist[1],int(ctlist[2]))
            shopdic[good.id]=good
            index+=1
        return shopdic
    def writeContentFiles(self):
        str1=''
        for key in self.shopdic.keys():
            good =self.shopdic[key]
            ele =good.id+'|'+good.name+'|'+str(good.price)+'\n'
            str1=str1+ele
        f=open(self.path,'w',encoding='utf-8')
        f.write(str1)
        f.close()
    def addGoods(self):
        id=input('请输入商品编号：')
        if self.shopdic.get(id):
            print('该商品已存在，请重新选择')
            return
        name=input('请输入商品名称：')
        price=input('请输入商品价格：')
        good=Goods(id,name,price)
        self.shopdic[good.id]=good
        # self.writeContentFiles()
        print('商品添加成功')
    def deleteGoods(self):
        id=input('请输入商品编号：')
        if not self.shopdic.get(id):
            print('该商品不存在，请重新选择')
            return
        del self.shopdic[id]
        # self.writeContentFiles()
        print('商品删除成功')
    def showGoods(self):
        print('='*40)
        for key in self.shopdic.keys():
            print(self.shopdic[key])  
        print('='*40)
    def adminWork(self):
        info='''
        =============欢迎进入商场===========
            输入功能编号，您可以选择以下功能：
            输入“1”：显示商品的信息
            输入“2”：添加新的商品
            输入“3”：删除已有商品
            输入“4”：退出系统
        ====================================
        '''
        print(info)
        while True:
            code = input('请输入功能编号:>')
            if code =='1':
                self.showGoods()
            elif code =='2':
                self.addGoods()
            elif code =='3':
                self.deleteGoods()
            elif code =='4':
                print('感谢您的使用，正在退出系统')
                self.writeContentFiles()
                break
            else:
                print('您的输入编号有误，请重新输入')
    def userWork(self):
        print('==========欢迎进入商场==========')
        print('您可以输入商品编号，将商品添加到购物车，输入编号为n则结账')
        self.showGoods()
        total=0
        while True:
            id = input(('请输入购买商品编号：'))
            if id =='n':
                    print("本次购买消费%d元，欢迎下次光临！"%total)
                    break
            if self.shopdic.get(id):
                    good = self.shopdic.get(id)
                    num = int(input('请输入购买数量：'))
                    total=total+good.price*num
            else:
                    print('您输入的商品编号有误，请重新输入')
    def login(self):
        print("==========欢迎登录商场系统==========")
        uname=input('请输入用户名：')
        if uname =='admin':
            password=input('请输入密码：')
            if password =='123456':
                print('欢迎您，admin管理员')
                self.adminWork()
            else:
                print('您输入的密码有误，请重新输入')
        else:
            print('欢迎你，%s用户'%uname)
            self.userWork()
if __name__=='__main__':
    path='shop.txt'
    shopManager=ShopManager(path)
    shopManager.login()
        
