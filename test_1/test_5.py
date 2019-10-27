#BMI計算

#========funtions==================
def input_val(message) -> int:
    val :varient = 0
    ret :int     = 0
    while ret == 0 :
        val = input(message)

        if not(str.isdecimal(val)) or int(val) <= 0:
            print("0以上の正数値を入力してください")
        else:
            ret = val
    return ret

#========main======================

#変数定義
height :int = 0
weight :int = 0
BMI    :int = 0
comment :str = ""

height = input_val("身長を入力してください[cm]  :")
weight = input_val("体重を入力してください[kg]  :")
BMI    = ( int(weight) *10000 / (int(height) ** 2 ) )

print("身長:{}".format(height))
print("体重:{}".format(weight))
print("BMI:{}".format(BMI))

if 25 >= BMI >= 18.5 :
    comment = "BMIは標準的な数値です。"
elif 18.5 > BMI :
    comment = "痩せています。"
else :
    comment = "太っています。"

print(comment)
