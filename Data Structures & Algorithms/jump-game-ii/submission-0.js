class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    jump(nums) {
        let jumps = 0;
        let farthest = 0;
        let currEnd = 0;
        for (let i = 0; i < nums.length - 1; i++){
            farthest= Math.max(farthest, i + nums[i]);

            if (i == currEnd){
                jumps++;
                currEnd = farthest
            }
        }
        return jumps
    }
}
