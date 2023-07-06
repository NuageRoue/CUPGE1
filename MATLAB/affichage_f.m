f = @(x) x.^3 + 4*x.^2 - 10;

x = linspace(0, 5, 100);
y = f(x);
grid on
plot(x, y);
title('Courbe de f(x) = x^3 + 4x^2 - 10');
xlabel('x');
ylabel('f(x)');
