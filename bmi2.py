#输入身高体重
height=float(input("请输入您的身高："))  
weight=float(input("请输入您的体重："))    
bmi=weight/(height*height)              #计算BMI指数
print("您的BMI指数为："+str(bmi))   #输出BMI指数

#判断身材是否合理
if bmi<18.5:
     print("体重过轻")
if bmi>=18.5 and bmi<24.9:
     print("正常范围")
if bmi>=24.9 and bmi<29.9:
     print("体重过重")
if bmi>=29.9:
     print("肥胖")
