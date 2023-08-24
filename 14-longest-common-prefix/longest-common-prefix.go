func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	if len(strs) == 1 {
		return strs[0]
	}
	minLen := len(strs[0])
	for _, strng := range strs {
		if len(strng) < minLen {
			minLen = len(strng)
		}
	}
	commonStr := ""
	for i := 0; i < minLen; i++ {
		chr := strs[0][i]
		for _, strng := range strs {
			if strng[i] != chr {
				return commonStr
			}
		}
		commonStr = commonStr + string(chr)
	}
	return commonStr
}