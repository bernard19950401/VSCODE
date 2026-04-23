try:
    num = float(input("请输入一个数字："))
    print(f"{num} 的平方是：{num ** 2}")
except ValueError:
    print("输入无效，请输入数字。")
