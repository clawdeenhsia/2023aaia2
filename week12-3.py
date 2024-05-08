# week12-3.py 質數的篩子法
table = [True]*240000
ans = 0
for i in range(2, 240000): #找出所有可能的質數，質數不會被整除，表格裡還留著繼承權
  if table[i]==True: #找到了，他是質數，因為沒有被國王殺死，當國王
    ans += 1
    for k in range(i*i, 240000, i): table[k] = False #國王繼位後，把他的兄弟殺光光
print('找到', ans, '個質數')
