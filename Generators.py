import sympy as sm
from sympy import *
import math
import numpy as np
from IPython.display import display, Markdown, Latex
a,b,x,y,M,z,i,s ,c, v ,q, pi= sm.symbols('a b x y M z i s c v q pi')
function = "z**2"
def Complex_Function(z):
    F_ofZ=eval(function)
    return F_ofZ
F_ofAandB = Complex_Function(a+b)
F_ofAandBe = Complex_Function(a+b*exp(-x))
F_ofandbexa = Complex_Function(a+b*exp(-x/c))
DerivativeN1_Func = sm.diff(F_ofAandBe , a)
DerivativeN2_Func = sm.diff(DerivativeN1_Func , a)
print("The function you entered is")
display(Complex_Function(z))
print("\033[1m The Linear Generator Number 1 will be \033[0m")
if DerivativeN1_Func ==0:
      display(Latex(r"$y''(x)+y(x)=\pi($"),F_ofAandB - F_ofAandBe + M)
elif DerivativeN2_Func ==0:
    display(Latex(r"$y''(x)+y(x)=\pi ($") ,F_ofAandB - F_ofAandBe + M - b * exp(-x) * DerivativeN1_Func)
else:
    display(Latex(r"$y''(x)+y(x)=\pi$") ,sm.factor(F_ofAandB - F_ofAandBe + M - b * exp(-x) * DerivativeN1_Func - b**2 * exp(-2*x) * DerivativeN2_Func) )
print("\033[1m The Linear Generator Number 2 will be \033[0m")
if DerivativeN2_Func ==0:
    display(Latex(r"$y''(x)+y'(x)=0$"))
else:
    display(Latex(r"$y''(x)+y'(x)=\pi $"), -b**2 * exp(-2*x) *DerivativeN2_Func)
print("\033[1m The Linear Generator Number 4 will be \033[0m")
if DerivativeN1_Func ==0:
    display(Latex(r"$y''(x)+ y'(\frac{x}{a}) - y(x) =\pi( $"),(F_ofAandBe-F_ofandbexa + 2*M))
elif DerivativeN2_Func ==0:
    display(Latex(r"$y''(x)+y'(\frac{x}{a}) - y(x) = \pi($"),(F_ofAandBe - F_ofandbexa + 2*M - b* exp(-x) * DerivativeN1_Func))
else:
    display(Latex(r"$y''(x)+y'(\frac{x}{a}) - y(x) =\pi $"), (F_ofAandBe-F_ofandbexa + 2*M - b* exp(-x) * DerivativeN1_Func - 
                                                              b**2 * exp(-2*x) * DerivativeN2_Func))
print("\033[1m The Non-Linear Generator Number 2 will be \033[0m")
if DerivativeN1_Func ==0:
    display(Latex(r"$(y''(x))^q + (y'(x))^v = 0$"))
elif DerivativeN2_Func ==0:
    display(Latex(r"$(y''(x))^q + (y'(x))^v = {\pi}^q ($"), (-b*exp(-x)* DerivativeN1_Func)**q ,  Latex(r"$+\,{\pi}^v$") , 
            (b*exp(-x)*DerivativeN1_Func)**v)
else:
    display(Latex(r"$(y''(x))^q + (y'(x))^v = (\pi)^q ($"), 
        (-b*exp(-x) * DerivativeN1_Func - b**2 * exp(-2*x) * DerivativeN2_Func)**q ,Latex(r"$+\,{\pi}^v$"), (b*exp(-x)* DerivativeN1_Func)**v )
print("\033[1m The Non-Linear Generator Number 6 will be \033[0m")
if DerivativeN1_Func == 0:
    display(Latex(r"$(sin(y''(x))) + (y(x)) = \pi $"), (F_ofAandB - F_ofAandBe + M))
elif DerivativeN2_Func ==0:
    display(Latex(r"$(sin(y''(x))) + (y(x)) = \pi $"), (F_ofAandB - F_ofAandBe + M)
                                            + sin( pi * (-b*exp(-x) * DerivativeN1_Func))) 
else:
    display(Latex(r"$(sin(y''(x))) + (y(x)) = \pi $"), (F_ofAandB - F_ofAandBe + M)
                                            + sin( pi * (-b*exp(-x) * DerivativeN1_Func)
                                            -b**2 *exp(-2*x)*DerivativeN2_Func))
print("\033[1m The Non-Linear Generator Number 7 will be \033[0m")
if DerivativeN1_Func ==0:
    display(Latex(r"$ e^{y''(x)} + e^{y'(x)} = 2 $"))
elif DerivativeN2_Func ==0:
    display(Latex(r"$ e^{y''(x)} + e^{y'(x)} = $"), exp(pi * (-b*exp(-x)* F_ofAandBe ))
                                                + exp(pi *(b*exp(-x) * DerivativeN1_Func)))
else:
    display(Latex(r"$ e^{y''(x)} + e^{y'(x)} = $"), exp(pi * (-b*exp(-x)* F_ofAandBe -b**2 * exp(-2*x) * DerivativeN2_Func ))
                                                + exp(pi *(b*exp(-x) * DerivativeN1_Func)))
    
print("\033[1m The Non-Linear Generator Number 10 will be \033[0m")
if DerivativeN1_Func ==0:
    display(Latex(r"$ y(\frac{x}{c}) + ln(y'(x))= \pi $"), (F_ofAandB - F_ofandbexa + M ))
else:
    display(Latex(r"$ y(\frac{x}{c}) + ln(y'(x))= \pi $"), (F_ofAandB - F_ofandbexa + M + ln(b*exp(-x) 
                                                    * DerivativeN1_Func ) ) )
print("The solution of the differential equations mentioned above is: ")
display(Latex(r"$y(x) = \pi($"), F_ofAandB - F_ofAandBe+M )
                         