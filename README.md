# DerivativeCalc

This is a program designed to be able to take the derivative of most functions. There were some necessary restrictions in input I needed to make, though, as my string parsing ability isn't quite up to snuff yet. 
<br/><br/>Therefore, if you want to enter a term raised to a power (non-poly power, anyway), you must do so like: [terms]^(power). And if you want to enter a product, you must write: < terms >*< terms >. As you might expect, a quotient is done like this: < terms >/< terms >.
<br/><br/>For example, if you wanted to differentiate (x^2+2)^3, you'd need to type: [x^2 + 2]^(3). I haven't implemented logarithmic differentiation, but I don't think it will be too difficult. I just have to check if float(exponent) generates an error.
<br/><br/>To conclude, this program is still a work in progress, but I'm happy with what I've made thus far.
