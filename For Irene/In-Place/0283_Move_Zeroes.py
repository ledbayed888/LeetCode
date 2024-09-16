# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         i = 0
#         for j in range(len(nums)):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void moveZeroes(int* nums, int numsSize){
    int i = 0;
    for(int j = 0; j < numsSize; j++){
        if(nums[j] != 0){
            swap(&nums[j], &nums[i]);
            i++;
        }
    }

}
                
        
