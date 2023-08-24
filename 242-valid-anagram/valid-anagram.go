func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
	var sa = []rune(s)
	var ta = []rune(t)

	sort.Slice(sa, func(i, j int) bool { return sa[i] > sa[j] })
	sort.Slice(ta, func(i, j int) bool { return ta[i] > ta[j] })
	for i, chr := range sa {
		if chr != ta[i] {
			return false
		}
	}
	return true

}