还在担心自己的代码风格不规范, python black让你省心省力

假设你写的代码是这样
dic = {"a":1, "b":2,   "c":3, "d":"fffffffffffffffffffffffffffffffffffffffffffffffffffffff"}

使用black之后,自动帮你改成：
dic = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": "fffffffffffffffffffffffffffffffffffffffffffffffffffffff",
}

Black，代码格式化工具，如果你的代码不符合PEP8规范，它检测到不符合规范的代码风格直接就帮你全部格式化好
使用非常简单，安装成功后，和其他系统命令一样使用，只需在 black 命令后面指定需要格式化的文件或者目录就ok

安装
pip install black

使用
black my_file.py

注意：
black会格式化整个文件，不会格式化以#fmt:off 开头和以 #fmt:on 结尾的代码块，或者以 #fmt:skip 结尾的行

如果需要定制某些配置，可以编写pyproject.toml文件：
[tool.black]
line-length = 88
include = '\.pyi?$'

还可以与 pre-commit 集成，集成后 git commit 时自动帮你检测代码并自动格式化，格式化后本次commit失败，需要自己重新 git add,git commit
编辑.pre-commit-config.yaml文件
repos:
  - repo: local
    hooks:
      - id: black
        name: black
        language: system
