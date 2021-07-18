driving = input('請問你有沒有開過車?：')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #讓程式在這邊終止

age = input('請問你的年齡？')
age = int(age) #要記得數字跟字串不能比較,必須要型別轉換
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('逼逼逼', '警察來抓人喔')
elif driving == '沒有':
	if age >= 18:
		print('他媽的還不去考駕照')
	else:
		print('乖乖吸奶喔')