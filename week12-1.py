# week12-1.py
n = int(input('�п�J1�Ӽ�:'))
def isPrime(n):
  for i in range(2,n):  #�u��1��n�����㰣
    if n%i==0:
      return False
  return Ture  #�p�G���S�����ѡA�N�O���\

if isPrime(n): print('n�O���')
else: print('n���O���')
