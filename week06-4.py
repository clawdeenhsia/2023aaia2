int maxFrequencyElements(int* nums, int numsSize) {
    int a[101] = {}; //�έp�Ʀr�X�{�����ơA�@�}�l�O0(�C�Ӱ}�C��l�̡A���|��0)
    int best = 0;
    for(int i=0; i<numsSize; i++){
        int now = nums[i];
        a[now]++;
        if(a[now]>best) best = a[now];
    }
    int ans = 0;
    for(int i=0;i<numsSize;i++){
        int now = nums[i];
        if(a[now]==best) ans++;
    }
    return ans;
}

