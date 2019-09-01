#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time   :  2019/8/31
# @Author :  xuwei
# @Email  :  mrwaynexue@126.com
# @Note   :
import matplotlib.pyplot as plt

# 房屋属性参数
paras={'school':0, 'metro':0, 'price':1.4, 'area':100, 'life':65}
economic = {'tax':0,'inflation':0.10}
# 房产估值模型
def capital_assessment(paras, economic, n):
    '''
    :param paras:
    :param economic:
    :param n: 第n年
    :return:
    '''
    total = 2*100

    # 是否学区房, +

    # 是否地铁，+

    # 通货膨胀率，+
    total = total * (1 + 0.05) ** n

    # 折旧（与剩余年限有关），-
    # n==life，时，total=0，取直线折旧法
    total = total*(1-n/65)

    # 房产税（首套房免征）, -
    return total

def average_rent(total, n):
    '''
    :param total: 初始房租
    :param n: 租赁期限
    :return: 年（月）房租
    '''
    total = 3
    # 收入增长率，+
    total = total * (1 + 0.04) ** n
    # 房屋折旧
    total = total*(1-n/65)

    return total

# 净现值
def calc_npv(money, n, r):
    '''
    :param money:
    :param n: 第n年
    :param r: 贴现利率
    :return:  净现值
    '''
    return money/(1+r)**n

# 贷款等额本金
def avrage_capital(total, n, r):
    '''
    :param total: 总贷款金额
    :param n: 贷款年份
    :param r: 利率
    :return: 年（月）还款
    '''
    q = 1/(1+r)
    sn = q*(1-q**n)/(1-q)  # 等比级数求和
    x = total/sn
    return x

fig = plt.figure()
# 轴
ax = fig.add_subplot(111)
ax.set(xlim=[2019,2019+66], ylim=[0, 500], title="房屋价值变化", ylabel='房屋价值（万元）', xlabel='年份')
plt.show()

capital = [capital_assessment(paras, economic, i) for i in range(66)]


money = capital_assessment(paras, economic, 30)
print('房产30年后价值%s',money)
value_npv = calc_npv(money,30,0.04)
print('净现值')
print(value_npv)
rent = [average_rent(2.2, i) for i in range(1,31)]
print('30年租金收入%s',rent)
rent_npv = sum([calc_npv(rent[i],i+1, 0.04) for i in range(30)])
print('30年租金收入净现值%s',rent_npv)
print('净现值')
print(value_npv+rent_npv)

loan = [avrage_capital(200, 30, 0.05) for i in range(30)]
loan_npv = sum([calc_npv(loan[i], i+1, 0.04) for i in range(30)])
print('30年贷款净现值%s', loan_npv)
print('净现值')
print(loan_npv+100)

print(avrage_capital(100, 30, 0.05))
print('\n')
print(capital_assessment(paras,economic, 50))
