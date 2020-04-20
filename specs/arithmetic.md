Module Structure in PostBOL
-----------------------------

An example

Identification:
	function "Calculate Interest"

Import:
	const interest_rate .int(2)
	var balance int(4).int(2)

Data:
	var interest int(4).int(2)

Procedure:
	multiply balance by interest_rate giving interest

Export:
	interest

In this example, the module is a function called "Calculate Interest". The way is open for the module to be something other than a function. In this case, the module declares two imports, an item of data, a single line procedure, and a variable to be exported (returned) at the end of the program.
