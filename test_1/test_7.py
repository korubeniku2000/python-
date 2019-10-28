#2進数,16進数変換

#========funtions==================

#入力チェック
def input_val(message) -> int:
    val :varient = 0
    ret :int     = 0
    while ret == 0 :
        val = input(message)

        if not(str.isdecimal(val)) :
            print("数値を入力してください")
        else:
            ret = val
    return ret

#========main======================

#変数定義

val :int = input_val("数字を入力してください:")

print("{} = {}".format(val ,format(int(val),'08b')))
print("{} = {}".format(val ,format(int(val),'08x')))
