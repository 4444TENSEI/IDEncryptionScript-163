import execjs

# 调用main.js，传入id转换为params和encSecKey
def getdata(id):
    node = execjs.get()
    ctx = node.compile(open("main.js", encoding="utf-8").read())
    # 将id转换为字符串
    exp = 'generate("' + str(id) + '")'
    pwd = ctx.eval(exp).split(",")
    data = {"params": pwd[0], "encSecKey": pwd[1]}
    print("生成参数为:")
    print(data)
    return data

getdata(666666)
