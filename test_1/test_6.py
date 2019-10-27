#入力した数分の星を表示して1つずつ塗りつぶす。

#========import====================
import sys,time

#========funtions==================

#入力チェック
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

#星表示
def show_stars(count , input_star) -> str:
    star_count : int = 0
    star :str = "{} :".format(count + 1)
    for star_count in range(0 , int(count) + 1):
        star += "★ "
    for star_count in range(int(star_count) , int(input_star) -1 ):
        star += "☆ "

    return star
    
#========main======================

#変数定義
input_star :int = 0
input_star = input_val("表示させる★ の数を入力してください:")

for count in range(0,int(input_star)):
    sys.stdout.write("\r%s" % show_stars(count , input_star))
    sys.stdout.flush()
    time.sleep(1)

#プログラム終了後に入力行と被ってしまうため、改行挿入
print()
