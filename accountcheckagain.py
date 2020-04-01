import openpyxl as xl
from openpyxl.styles import  PatternFill
import operator

def myinvoice():
    mylist = []  # 该列表存放我方表格中的发票信息
    mymoneylist = []  # 该列表存放我们金额信息，位置与mylist中的发票信息位置一一对应。
    wb = xl.load_workbook(f'{myfilename}.xlsx')
    sheet = wb['应收款明细表']  # 注意这里的sheet名
    maxrow = sheet.max_row

    for row in range(2,maxrow+1):
        money = sheet[f'Q{row}'].value
        invoice = str(sheet[f'G{row}'].value)
        if len(invoice) == 7:
            invoice='0'+invoice
        elif len(invoice) ==6:
            invoice='00'+invoice
        mylist.append(invoice)
        mymoneylist.append(money)
    return mylist,mymoneylist

def customiovmoney(filename):
    wb = xl.load_workbook(f'{filename}.xlsx',data_only=True)
    sheet = wb['Sheet1']
    maxrow = sheet.max_row
    cusmoney = []
    for i in range(2,maxrow+1):
        cell = sheet[f'D{i}'].value
        if cell is not None:
            cmoney = round(float(sheet[f'D{i}'].value),2)
            cusmoney.append(cmoney)
        else:
            cusmoney.append(cell)
    return cusmoney

def custominvinfo(filename):
    wb = xl.load_workbook(f'{filename}.xlsx',data_only=True)
    sheet = wb['Sheet1']
    maxrow = sheet.max_row
    invinfo = []
    binfo= []
    for i in range(2,maxrow+1):
        cell =sheet[f'B{i}'].value
        if len(str(cell)) == 7:
            cell = '0'+str(cell)
        elif len(str(cell))==6:
            cell='00'+str(cell)
        if cell is None:
            binfo.append(i)
            invinfo.append(cell)

        else:
            cell = str(cell).split('-')[0]
            invinfo.append(cell)
    return binfo,invinfo

def datadeal(binfo,invinfo,cusmoney):
    countmoney = []
    for i in range(len(cusmoney)):
        if i + 2 in binfo:
            if cusmoney[i] is not None:
                countmoney.append(cusmoney[i])
    return countmoney


def checkaccount(custominvinfo,custommoneyinfo,myinvinfo,mymoneyinfo):
    length = len(custommoneyinfo)
    teminvinfo = []
    for i in range(length):
        if custominvinfo[i] is not None:
            if custominvinfo[i] in teminvinfo:
                ind = teminvinfo.index(custominvinfo[i])
                teminvinfo[ind+1]+=round(custommoneyinfo[i],2)
            else:
                teminvinfo.append(custominvinfo[i])
                teminvinfo.append(round(custommoneyinfo[i],2))

    for i in range(length):
        if custominvinfo[i] in myinvinfo:
            ind =myinvinfo.index(custominvinfo[i])
            ind2 = teminvinfo.index(custominvinfo[i])
            if mymoneyinfo[ind] == round(teminvinfo[ind2+1],2):
                # print('没问题')
                print(f'没有问题，发票号为：{custominvinfo[i]},我方金额：{mymoneyinfo[ind]},对方金额：{teminvinfo[ind2 + 1]}')
                fillcell(True,i,mymoneyinfo[ind])
            else:
                fillcell(False, i, mymoneyinfo[ind])
                spacefill(40)
                print(f'有问题，发票号为：{custominvinfo[i]},      我方金额：{mymoneyinfo[ind]},对方金额：{teminvinfo[ind2+1]}')

def spacefill(num):
    for i in range(num):
        print(' ')

def fillcell(type,ind,money): # 该函数是对正确的金额与错误的金额两种情况进行颜色填充，绿色表示金额正确，红色表示错误。
    wb = xl.load_workbook(f'{customfilename}.xlsx')
    sheet = wb['Sheet1']

    if type is True:
        fill = PatternFill("solid", fgColor="ADFF2F") # 颜色的值参考网址：http://www.114la.com/other/rgb.htm
        # for i in fillnum:
        sheet[f'E{ind+2}'].fill = fill
        sheet[f'E{ind+2}'].value = money
        wb.save(f'{customfilename}.xlsx')

    else:
        fill = PatternFill("solid", fgColor="CD3333")
        # for i in fillnum:
        sheet[f'E{ind+2}'].fill = fill
        sheet[f'E{ind+2}'].value = money
        wb.save(f'{customfilename}.xlsx')

def main():
    binfo,invinfo = custominvinfo(customfilename)
    cusmoney= customiovmoney(customfilename)
    countmoney = datadeal(binfo,invinfo,cusmoney)
    mylist,mymoneylist = myinvoice()  # mylist列表存放我方所有发票信息，mymoneylist存放对应的金额
    checkaccount(invinfo,cusmoney,mylist,mymoneylist)


if __name__ == '__main__':
    print('-----------------------------------------------------------------------------------------------------')
    print('注意事项如下：')
    print('''
         1. 我方明细表与对方明细表以及本程序必须防止在同一文件夹下；
         2. 输入表名时不需要输入后缀名；
         3. 我方表的sheet名为：应收款明细表，对方表的sheet名为：Sheet1；
         4. 我方表中发票信息在G列，金额信息在Q列。客户表中发票信息在B列，金额在D列，标记信息在E列。
         ''')
    print('-----------------------------------------------------------------------------------------------------')

    myfilename= input('请输入我方明细表名：')
    customfilename=input('请输入客户表名：')

    res = []
    lastres = []
    strlist=[]
    moneylist = []
    main()
