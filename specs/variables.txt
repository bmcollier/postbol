Variables in PostBOL
--------------------

The PIC name in COBOL is a bit opaque, so we're renaming it to both var and const, to give us variables and constants.

Variables are defined in the data section, but Python-like colons are added to denote the beginning of the section, like so:

Identification:
	name "Calculate Interest"

Data:
	const 	interest .int(8)
	var 	balance int(4).int(2)

In the above example, the constant named "interest" will be a decimal less than 1 with up to eight decimal places. The variable named "balance" will be an integer less than 10000 - up to 4 integer digits, followed by two integer decimal places.


