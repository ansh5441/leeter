func categorizeBox(length int, width int, height int, mass int) string {
    sideLim := 10000
	volumeLim := 1000000000
    isBulky := length >= sideLim || width >= sideLim || height >= sideLim || length*width*height >= volumeLim
	isHeavy := mass >= 100

	if isBulky && isHeavy {
		return "Both"
	}
	if !(isBulky || isHeavy){
		return "Neither"
	}
	if isBulky {
		return "Bulky"
	}
	return "Heavy"
    
}