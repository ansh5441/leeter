func twoSum(nums []int, target int) []int {
	sumMap := make(map[int]int)
	for i, t := range nums {
		if index, present := sumMap[t]; present == true {
			return []int{index, i}
		}
		sumMap[target-t] = i
	}
	return []int{}
}