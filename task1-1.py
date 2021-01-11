# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2021/1/11 9:45 下午
# @File       : task1-1.py
# @Description:

# step 1：导包
from py2neo import Graph, Node, Relationship

# step 2：构建图
g = Graph("http://localhost:7474",auth=("neo4j","password"))
# step 3：创建节点
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
# step 4：创建边
ab = Relationship(a, "KNOWS", b)
# step 5：运行
tx.create(ab)
tx.commit()

print(g.nodes.match("Person", name="Alice").first())
print(g.match(nodes=None, r_type=None, limit=None).all())

# # Node
# #获取key对应的property
# x=a['name']
# print(x)
#  #设置key键对应的value，如果value是None就移除这个property
# a["key"] = "happy"
#  #也可以专门删除某个property
# del a["key"]
# #返回node里面property的个数
# len(a)
# #返回所以和这个节点有关的label
# labels=a.labels
# #删除某个label
# a.labels.remove('labelname')
# #将node的所有property以dictionary的形式返回
# dict(a)