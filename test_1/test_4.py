#テストの合計、平均計算

#======functions=========================
def set_score(subject):
    score = ""
    while score != "不参加" and not(str.isdecimal(score)):
        print(subject,"の点数を入力してください")
        print("不参加の場合は何も入力せずにEnterキーを押下してください")
        score = input("点数：")

        if not(str.isdecimal(score)):
            print()
            print("点数を入力してください")

        if score == "":
            score = "不参加"


    return score

#======main==============================

#変数定義
subjects = ["国語","算数","理科","社会","英語"]
scores = [0,0,0,0,0]
total = 0
average = 0

#点数入力
for count in range(len(subjects)):
    scores[count] = set_score(subjects[count])

#改行
print()

#点数表示と合計,平均計算
print("/////////各教科の点数//////////////")
for count in range(len(subjects)):
    print(subjects[count],":",scores[count])
    if scores[count] != "不参加":
        total += int(scores[count])
        average += 1

#合計,平均点表示
print()
print("合計:",total)
print("平均:",total // average)
