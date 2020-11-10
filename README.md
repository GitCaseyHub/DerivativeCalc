# DerivativeCalc

This is a program designed to be able to take the derivative of most functions. There were some necessary restrictions in input I needed to make, though, as my string parsing ability isn't quite up to snuff yet. 
<br/><br/>Therefore, if you want to enter a term raised to a power (non-poly power, anyway), you must do so like: [terms]^(power). And if you want to enter a product, you must write: < terms > * < terms >. As you might expect, a quotient is done as: < terms > / < terms >. For example, if you wanted:
<br/><br/>to differentiate (x^2+2)^3, you'd need to type: [x^2 + 2]^(3).
<br/>to differentiate (x+2)*(e^x), you'd need to type: <x+2>*<exp(x)>.
<br/>to differentiate (x+1)/(tan(x)), you'd need to type: <x+1>/<tan(x)>
<br/><br/>To conclude, I think this program works completely except for maybe some clean printing for more complex functions.
