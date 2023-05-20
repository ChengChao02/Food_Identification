import pymysql
import pandas as pd


def read_txt(inputpath):
    with open(inputpath, 'r', encoding='utf-8') as infile:
        data2 = []
        for line in infile:
            data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
            print(data_line)
            data2.append([int(i) for i in data_line])
        print(data2)
        # 输出：[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        # 每个字符分开读取
        data = data2
        for i in range(len(data2)):
            data.append(data2[i][0])
        # 输出：[['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10']]
        print(data)


# 建立数据库连接
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='zcc147852369',
    db='food',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()

# 1、从数据库中查询
sql = "SELECT * FROM test"
cursor.execute(sql)  # 提交
print('数据总数：', cursor.rowcount)
rr = cursor.fetchall()  # 将所有的结果放入rr中
for row in rr:
    print("ID=%s, 姓名=%s, 名字=%s" % row)

names = ["apple", "banana", "egg", "carrot", "potato", "meat",
                         "kola", "milk", "strawberry", "orange","aubergine", "xuebi"]
# 2、数据库中插入数据
cnt = 1
insert = "INSERT INTO test values({},'{}');".format(cnt, names[1])
cursor.execute(insert)  # 执行
conn.commit()  # 刷新
cursor.execute(sql)  # 提交
rr = cursor.fetchall()  # 将所有的结果放入rr中
for row in rr:
    print("ID=%s, 姓名=%s" % row)
 
# 数据库连接和游标的关闭
conn.close()
cursor.close()
'''
names = ["apple", "banana", "egg", "carrot", "potato", "meat",
                         "kola", "milk", "strawberry", "orange","aubergine", "xuebi"]

for i in range(7):
    print("thiei  si {}".format(names[i]))
'''