# week12-3.py ��ƪ��z�l�k
table = [True]*240000
ans = 0
for i in range(2, 240000): #��X�Ҧ��i�઺��ơA��Ƥ��|�Q�㰣�A�����ٯd���~���v
  if table[i]==True: #���F�A�L�O��ơA�]���S���Q��������A����
    ans += 1
    for k in range(i*i, 240000, i): table[k] = False #����~���A��L���S�̱�����
print('���', ans, '�ӽ��')
