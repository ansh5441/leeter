
type mapKey struct {
	amt   int
	index int
}

func change(amount int, coins []int) int {
	mapOfHelp := make(map[mapKey]int)
	return changeHelp(amount, coins, 0, &mapOfHelp)
}

func changeHelp(amount int, coins []int, index int, dpMap *map[mapKey]int) int {
	if amount < 0 {
		return 0
	}
	if amount == 0 {
		return 1
	}
	if val, ok := (*dpMap)[mapKey{amount, index}]; ok {
		return val
	}
	numWays := 0
	for i, c := range coins {
		if i >= index {
			numWays += changeHelp(amount-c, coins, i, dpMap)
		}
	}
	(*dpMap)[mapKey{amount, index}] = numWays
	return numWays
}