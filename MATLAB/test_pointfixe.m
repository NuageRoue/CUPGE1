% test point fixe :

fun1 = @(x) x^3 + 4 * x^2 -10 + x
fun2 = @(x) (-4 * x^2 +10)^(1/3)
fun3 = @(x) 1/2 * sqrt(-x^3 +10)

trueValue = roots([1 4 0 -10]);
trueValue = trueValue(3)

%fun1 :

[xfun1, iter_fun1] =  fixedPoint_func(fun1, 0, 100, 10^-3, trueValue)
errfun1 = abs(trueValue - xfun1)

[xfun2, iter_fun2] =  fixedPoint_func(fun2, 0, 100, 10^-3, trueValue)
errfun2 = abs(trueValue - xfun2)


[xfun3, iter_fun3] =  fixedPoint_func(fun3, 0, 100, 10^-3, trueValue)
errfun3 = abs(trueValue - xfun3)

trueValue = roots([1 4 0 -10])

