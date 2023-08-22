func convertToTitle(columnNumber int) string {
    alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	var result string
	for columnNumber > 0 {
		columnNumber--
		result = string(alphabet[columnNumber%26]) + result
		columnNumber /= 26
	}
	return result
    
}