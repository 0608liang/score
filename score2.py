#只能輸入 不知道 或 數字 兩種型態
Target = input('請輸入學校最低錄取分數 : ')
Target = int(Target)

Chinese = 62.6
English = 42.8
Math = input('請輸入你的數學成績 :')
Physics = input('請輸入你的物理成績 :')
Chemistry = input('請輸入你的化學成績 :')

if Math == "不知道" and Physics == "不知道" and Chemistry == "不知道" :
	Average = ( Target - Chinese - English ) / 3
	print('你剩餘科目平均需要達到', Average, "分")

elif Math == "不知道" and Physics == "不知道" and Chemistry != "不知道" :
	Chemistry = int(Chemistry)
	Average = ( Target - Chinese - English - Chemistry ) / 2
	print('你剩餘科目平均需要達到', Average, "分")

elif Math == "不知道" and Physics != "不知道" and Chemistry == "不知道" :
	Physics = int(Physics)
	Average = ( Target - Chinese - English - Physics) / 2
	print('你剩餘科目平均需要達到', Average, "分")

elif Math != "不知道" and Physics == "不知道" and Chemistry == "不知道" :
	Math = int(Math)
	Average = ( Target - Chinese - English - Math) / 2
	print('你剩餘科目平均需要達到', Average, '分')

elif Math != "不知道" and Physics != "不知道" and Chemistry == "不知道" :
	Math = int(Math)
	Physics = int(Physics)
	Average = ( Target - Chinese - English - Math - Physics )
	print('你剩餘科目平均需要達到', Average, '分')

elif Math != "不知道" and Physics == "不知道" and Chemistry != "不知道" :
	Math = int(Math)
	Chemistry = int(Chemistry)
	Average = ( Target - Chinese - English - Math - Chemistry )
	print('你剩餘科目平均需要達到', Average, '分')

elif Math == "不知道" and Physics != "不知道" and Chemistry != "不知道" :
	Physics = int(Physics)
	Chemistry = int(Chemistry)
	Average = ( Target - Chinese - English - Physics - Chemistry)
	print('你剩餘科目平均需要達到', Average, '分')
