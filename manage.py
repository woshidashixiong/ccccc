import json

dic = {"status": "OK", "count": 20, "results": [{"age": 27, "name": "aex", "lactose_intolerant": True}, {"age": 29, "name": "jil", "lactose_intolerant": False}]}

# 普通dump
print(json.dumps(dic))
'''
输出
{'status': 'OK', 'count': 20, 'results': [{'age': 27, 'name': 'aex', 'lactose_intolerant': True}, {'age': 29, 'name': 'jil', 'lactose_intolerant': False}]}
'''

# 加上 indention参数
print(json.dumps(dic,indent=2))
'''
{
  "status": "OK",
  "count": 20,
  "results": [
    {
      "age": 27,
      "name": "aex",
      "lactose_intolerant": true
    },
    {
      "age": 29,
      "name": "jil",
      "lactose_intolerant": false
    }
  ]
}
'''

这样无论是打印输出还是写入到文件都很美观，易于阅读

