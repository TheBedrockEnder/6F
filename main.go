package main

import ("fmt"
)

func tax1(base float64) float64{
	var temp float64
	var temp2 float64
	if base <= 12570 {
		temp = base
	}
	if base >= 12570 {
		temp = 12570
		base = base - 12570
		if base > 0 {
			temp2 = base
			if temp2 > 37700{
				temp2 = 37700
			}
			base = base - temp2
			temp2 = 0.8 * temp2
			temp = temp + temp2
		}
		if base > 0 {
			temp2 = base
			if temp2 > 74870{
				temp2 = 74870
			}
			base = base - temp2
			temp2 = 0.6 * temp2
			temp = temp + temp2
		}
		if base > 0 {
			temp2 = base
			temp2 = 0.55 * temp2
			temp = temp + temp2
		}
	}
	return temp
}

func NI(base float64) float64{
	var temp float64
	var tempoutput float64
	switch {
		case base >= 50456.68:
			temp = 50456.68 - 12627.21
			base = base - 50456.68
			tempoutput = temp * 0.08
			temp = base * 0.02
			tempoutput = tempoutput + temp
		case base >=12627.21:
			base = base - 12627.21
			base = base * 0.08
			tempoutput = base
		case base <= 12627.21:
			tempoutput = 0
	}
	return tempoutput
}

func calctotal(afterTax float64, NIcost float64) float64{
	var temp float64
	temp = afterTax - NIcost
	return temp
}

func main() {
	var usrInput float64
	fmt.Scan(&usrInput)
	fmt.Println(calctotal(tax1(usrInput), NI(usrInput)))
}
