int maxFrequencyElements(int* nums, int numsSize) {
    int a[101] = {}; //�έp�Ʀr�X�{�����ơA�@�}�l�O0(�C�Ӱ}�C��l�̡A���|��0)
    int best = 0;
    for(int i=0; i<numsSize; i++){
        int now = nums[i];
        a[now]++;
        if(a[now]>best) best = a[now];
    }
    int ans = 0;
    for(int i=1;i<=100;i++){
        if(a[i]==best) ans+=a[i];
    }
    return ans;
}



///int a[101] ={};
///int best = 0;
///for(int i=0 ;i<numsSize; i++){
  ///  a[nums[i]] ++;
    ///if(a[nums[i]]>best) best=a[nums[i]];
///}
///int ans=0;
///for(int i=1;i<101;i++){
   ///     if(a[i]==best) ans++;
///}
///return ans;
