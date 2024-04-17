class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #�n����Ӫ� ��0....25��Ӧr��a....z
        table = "abcdefghijklmnopqrstuvwxyz" #�r����Ӫ�
        def helper(root,nowStr):
           # if root==None: return nowStr #��U�S���F��� �k��ֿn���r�� �N�O���G
            nextStr = table[root.val] + nowStr
            if root.left==None and root.right==None: return nextStr
            if root.left==None: return helper(root.right, nextStr) #���䪺���G
            if root.right==None: return helper(root.left, nextStr) #�k�䪺���G
            #�H�U�O���d�����p�A���k�䳣������A�N�n���䳣��A�A��p�����װe�X�h
            left = helper(root.left, nextStr)
            right = helper(root.right, nextStr)
            return min(left,right) #���G�p�� ����return�^�h
        return helper(root,'')

        #print("table[0] is", table[0]) #�u�O���ոլ�
        #print("table[25] is", table[25])  #�u�O���ոլ�
        return helper(root,'')   #�u�O���ոլ�
