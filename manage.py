import pandas as pd

# ===================读========================

df = pd.read_csv(
    filepath_or_buffer=r"C:\Users\lwx1089434\Desktop\workspace\tests\222.csv",
    dtype=str, #所有字段都已str形式读取，指定某种字段{"age":int}
    sep=",",#该参数代表数据的分隔符,csv文件默认为逗号
    skiprows=0,#该参数代表跳过数据文件的第一行不读
    nrows=15,#nrows 只读前n行,若不指定,读取全部内容,
    parse_dates=[],#将指定的列识别为日期格式,若不指定,时间数据将全会一字符串形式读入,
    index_col=[],#将指定列设为index,若不指定,index 默认为0,1,2
    usecols=["a", "b", "c", "d"],#读取指定的几列数据,其他不读,若不指定,读入全部列
    error_bad_lines=False,#当某行数据有问题,报错,设定false时,不报错直按跳过该行当数据比较脏乱的时候用这个
    na_values="NULL",#将数据中的nutl识别为空值
)

# ===================设置输出格式================

pd.set_option("expand_frame_repr",False) # 当行太多时不换行
pd.set_option("max_colwidth",8) # 设置每一行的最大宽度，恢复原设置方法pd.reset_option("max_colwidth")

# ===================类型转换===================

df = df.astype({
    "start_time": "datetime64",
    "age": "int",
    "value": "float32"
})

# ===================查看数据====================

print(df)
print(df.columns.values.tolist())   # 输出列名集合
print(df.columns.tolist())          # 输出列名集合
print(df.shape)                     # 输出行数和列数 (5,4) 5行4列
print(df.index)                     # 输出索引 RangeIndex(start=0, stop=4, step=1)
print(df.dtypes.to_dict())          # 输出 每一列的数据类型 {'a': dtype('int64'), 'b': dtype('int64'), 'c': dtype('int64'), 'd': dtype('int64')}
print(df.head(1))                   # 查看前3行的数据，默认为5
print(df.tail(1))                   # 查看最后3行的数据，默认为5
print(df.sample(frac=0.5))          # 随机抽取3行，想要固定比例的话，可以用frac参数
print(df.describe())                # 对每一列数据有一个直观感受，只会对数字类型的列有效
print(df.get("a").tolist())         # 取某一列数据


# ========================取数据================================

#取行数据
print(df[0:1])                      #取 第一行 通过index
print(df["a":"b"])                  #取 第一行 通过自定义index
print(df[[True,True,False,False]])  #选取 前2行 通过布尔数组
#取列数据
df["name"]                          #取name列所有数据
df[["name",'age']]                  #选取name,age两列数据
df[["name",'age']].values.to_list() #选取name,age两列数据
df[lambda df: df.columns[0]]        # 取第一列数据
#取行&列数据
df.loc["a",:]                       #取索引为a的行（包含所有列） ,前筛选行 ,后筛选列
df.loc["a":"d",:]                   #取索引从a到d的所有行
df.loc[["a","b","c"],:]             #取索引为a或b或c的行
df.loc[df["age"]>30,["name","age"]] #取age > 30的姓名和年龄
df.loc["a","name"]                  #取索引为a的行name列
df.iloc[1,:]                        # 选取第二行
df.iloc[:3,:]                       # 选取前3行
df.iloc[:,1]                        # 选取第2列
#单元格选取
df.at["b","name"]                   # 选取b行的name列 只能使用标签索引，即自定义索引
df.iat[1,0]                         # 选取第二行第一列  只能使用整数索引


# =========================筛选数据===============================

df[ df["age"] > 30]                                  # 筛选age > 30
df[(df["age"] > 30) & (df["isMarried"] == "no")]     # age > 30 并且 isMarried 为no
df[(df["age"] == 30) | (df["age"] == 20)]            # age = 30 或者 age =20
df[df["a"].apply(lambda x:x[2] == "f")]              #  结合apply过滤数据,a列的第二个字符为f
df[df["a"].isin(["a1","a2","a3"])]                   # a in ["a1","a2","a3"]
df[~df["a"].isin(["a1","a2","a3"])]                  # a not in ["a1","a2","a3"]
df[df["a"].str.strip().isin(["a1","a2","a3"])]       # a.strip() in ["a1","a2","a3"]

# =======================遍历数据===============================

#for column in df                 # 遍历列名，通过df[column]获取该列所有数据
#for column,data in df.items()    # 遍历列名，data是该列所有数据,data[0]取第一个数据
#for index,row in df.iterrows()   # 生成器，迭代数据帧的索引和行数据,可通过row[列名取值]
#for row in df.itertuples()       # row:Pandas(Index=0, Name='Alice', Age=25, City='New York'),命名元祖，可以[]或.列名取值，比iterrows()快
#for row in df.values             # ['wang1' 'hui' 300]


# ======================= 删除数据 =========================

df.drop( df[ df["a"] == "a1" ].index ) #drop通过index删除数据，删除掉a=a1的行，先筛选出a1,然后.index得到index集合，通过index集合再删除


# =======================分组===============================

df.groupby(["a","b"])        #安装a,b进行分组
df.groupby(["a","b"]).size() #安装a,b进行分组,统计每组的大小


# =======================去重===============================

df.drop_duplicates(subset=["a","b","c"]) #根据a,b,c列进行去重,keep="first"默认保留重复值的第一个,inplace=False,默认返回一个新的df


# =====================先分组再排序==========================

dic={
    "top":1, #1为最高优先级，top排在最前面
    "hi":2,
    "low":3
}
df = pd.read_csv("222.csv")
v = df.sort_values(by="c",key=lambda x: x.map(dic)).groupby(["a","b"]).first() #先按照a,b分组，每组内再按照c进行排序，然后每组内再取出一条数据,写法注意，必须先sort_values,再groupby

df["name"].value_counts().sort_values(ascending=False)[0:2].index.tolist()     # 找出数量前2名的name
df.groupby("name").size().sort_values(ascending=False)                         # 找出数量前2名的name for name,num in age.iteritems()

#=======================先分组再去重===========================

v = df.groupby(["a"]).apply(lambda x:x.drop_duplicates(subset=["b","c"])) #先根据a分组，每组内再根据b,c进行去重

#=======================先分组再agg统计=======================

v = df.groupby(["a","b"]).agg({"c":"count"}).sort_values(by="c")  #统计每组c的数量 等价于df.groupby(["a","b"]).size(),
age = df.groupby("name")["age"].agg(list).to_dict()               # 统计每组的年龄集合 {'name1': [20, 30], 'name2': [40], 'name3': [30]}


# ======================连表，多个数据处理========================

#concat通常只用于上下堆叠合并，如果上下字段不一致，取字段的并集，缺失字段填充Nan
pd.concat([pd.read_csv("csv1"),pd.read_csv(csv2)])
pd.concat(
    objs, # 要连接的对象，多个df的话，用列表的方式传入该参数[pd.read_csv("csv1"),pd.read_csv(csv2)]
    axis,  # 0->index,1->columns要连接的轴，0为上下堆叠，1为左右拼接
    join, #{‘inner’, ‘outer’}, 默认‘outer’。join='outer’表示外连接，保留两个表中的所有信息；join="inner"表示内连接，拼接结果只保留两个表共有的信息
    ignore_index,# bool，默认为 False。如果为 True，则不要沿连接轴使用索引值。结果轴将标记为 0, …, n - 1。如果您要连接对象，而连接轴没有有意义的索引信息，这将非常有用。请注意，连接中仍然尊重其他轴上的索引值。
    keys, # 键序列，默认无。如果通过了多个级别，则应包含 元组 。使用传递的键作为最外层构建层次索引。
    levels, # 序列列表，默认无。用于构造 MultiIndex 的特定级别（唯一值）。否则，它们将从密钥中推断出来。
    names, # 默认无。生成的分层索引中的级别名称。
    verify_integrity, #bool 值，默认为 False。检查新的连接轴是否包含重复项。相对于实际的数据连接，这可能非常昂贵。
    sort, # bool 值，默认为 False。如果连接为“外部”时尚未对齐，则对非连接轴进行排序。这在 join=‘inner’ 时无效，它已经保留了非串联轴的顺序。在 1.0.0 版更改: 默认情况下更改为不排序。
    copy, #bool 值，默认 True。如果为 False，则不要不必要地复制数据。

)
# merge 相当于sql的join,将不同的表安key关联到一起
pd.merge(left,right,how="inner",on=None,left_on=None,right_on=None,left_index=False,right_index=False,sort=True,
         suffixes=("_x","_y"),copy=True,indicator=False,validate=None)
# left,right ：要merge的dataframe或者有name的Series。
# how ：join类型，‘left’, ‘right’, ‘outer’, ‘inner’。
# on ：join的key，left和right都需要有这个key。
# left_on ：left的df或者series的key。
# right_on ：right的df或者seires的key。
# left_iddex,right_index ：使用index而不是普通的column做join。
# suffixes ：两个元素的后缀，如果列有重名，自动添加后缀，默认是(‘_x’, ‘_y’)。
# one-to-one 一对一关系，关联的key都是唯一的  结果条数1*1
# one-to-many 一对多关系，左边key唯一，右边key不唯一 结果条数 1*N
# many-to-many 多对多关系，左边右边都不是唯一的  结果条数M*N


# ===========================apply===============================================

apply(self,func,axis=0,raw=False,result_type=None,args=(),**kwargs)
# func 函数或lambda表达式，应用于每行或者每列
# axis 0 or index 表示函数处理的是每一列 axis 1 or columns 表示函数处理的是每一行
# row false,表示把每一列或行作为series传入函数中  true 表示接受的是ndarray数据类型
# result_type (expand,reduce,broadcast) expand:列表式的结果将被转化为列，reduce:如果可能的话，返回一个series,而不是展开类似列表的结果，这与expand相反 broadcast:结果将被广播到dataFrame的原始形状，原始索引和列将被保留
# args func的位置参数
# **kwargs func的关键字参数

# 将name=wangwei的score加上100
df.loc[df['name'] == 'wangwei', 'score'] += 100  #改变了原有df
df["score"] = df.apply(lambda x: x['score'] + 100 if x['name'] == 'wangwei' else x['score'], axis=1) # axis=1,x.name等于该行的索引axis=0,x.name等于列名，此时不能x[]取值
df["num"] = df["name"].apply(lambda value:value.split("name")[1]) #为df新增一列num,值为name列的最后一个字符



#==============================other============================

reset_index(drop=True) # 重置索引，drop=True删除原索引

unique() # 去重之后的不同值
#df["a"].unique() #a列去重之后的值
#df[df["a"] == "a1"]["b"].drop_duplicates().tolist()

nunique() # 去重后不同值的个数
rename(columns={"a":"b"}) # 重命名，将列a重命名为列b
dropna() # 删除有缺失值的行
fillna(0,inplace=True) # 将na填充为0，在原有的基础上修改
notnull() #判断值是否为null

# ===========================输出==================================

# 输出csv
to_csv("111.csv",index=False) # 转成csv,不写入索引
