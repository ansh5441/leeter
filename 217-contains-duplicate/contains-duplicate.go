func containsDuplicate(nums []int) bool {
	hm := make(map[int]bool)
	for _, n := range nums {
		if _, exists := hm[n]; exists {
			return true
		} else {
			hm[n] = true
		}
	}
	return false
}