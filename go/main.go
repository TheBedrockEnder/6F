package main

import ("fmt")

func tax1(base float64) float64{
	var temp float64
	var temp2 float64
	if base > 12570 {
		base = base - 12570
		if base > 0 {
			temp2 = base
			if temp2 > 37700{
				temp2 = 37700
			}
			base = base - temp2
			temp2 = 0.2 * temp2
			temp = temp + temp2
		}
		if base > 0 {
			temp2 = base
			if temp2 > 74870{
				temp2 = 74870
			}
			base = base - temp2
			temp2 = 0.4 * temp2
			temp = temp + temp2
		}
		if base > 0 {
			temp2 = base
			temp2 = 0.45 * temp2
			temp = temp + temp2
		}
	}
	return temp
}

func NI(base float64) float64{
	var temp float64
	var tempoutput float64
	switch {
		case base >= 50284:
			temp = 50284 - 12584
			base = base - 50284
			tempoutput = temp * 0.08
			temp = base * 0.02
			tempoutput = tempoutput + temp
		case base >= 12584:
			base = base - 12584
			base = base * 0.08
			tempoutput = base
		case base < 12584:
			tempoutput = 0
	}
	return tempoutput
}

func calctotal(tax float64, NIcost float64) float64{
	var temp float64
	temp = tax + NIcost
	return temp
}

func getIncome() float64{
	var amount float64
	var time string
	fmt.Println("how much money")
	fmt.Scan(&amount)
	fmt.Println("W/M/Y?")
	fmt.Scan(&time)
	for time != "W" && time != "M" && time != "Y" {
		fmt.Println("stop trying to break the code, answer correctly")
		fmt.Scan(&time)
	}
	if time == "W" {
		amount = amount * 52
	}
	if time == "M" {
		amount = amount * 12
	}
	return amount
}

func main() {
	var usrInput float64
	usrInput = getIncome()
	fmt.Println(calctotal(tax1(usrInput), NI(usrInput)))
}
