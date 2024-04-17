class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #要做對照表 把0....25對照字母a....z
        table = "abcdefghijklmnopqrstuvwxyz" #字母對照表
        def helper(root,nowStr):
           # if root==None: return nowStr #樹下沒有東西時 右邊累積的字串 就是結果
            nextStr = table[root.val] + nowStr
            if root.left==None and root.right==None: return nextStr
            if root.left==None: return helper(root.right, nextStr) #左邊的結果
            if root.right==None: return helper(root.left, nextStr) #右邊的結果
            #以下是健康的狀況，左右邊都有分支，就要兩邊都算，再把小的答案送出去
            left = helper(root.left, nextStr)
            right = helper(root.right, nextStr)
            return min(left,right) #結果小的 當答案return回去
        return helper(root,'')

        #print("table[0] is", table[0]) #只是先試試看
        #print("table[25] is", table[25])  #只是先試試看
        return helper(root,'')   #只是先試試看
