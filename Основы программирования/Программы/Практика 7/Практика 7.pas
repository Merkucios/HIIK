program Praktika_7;
var 
  x,res,n:real;
begin
  repeat
    writeln('Введите число в интервале [0..0.85]');
    readln(x)
  until (0 <= x) and (x <= 0.85) ;
  n := 0;
  
  repeat
    res := x;
    x := 1 / (x - 3 + sin(3.6 * x));
    writeln('Промежуточное значение: ', x:0:5);
    n := n + 1
  until abs(res - x) < 0.5e-4;
  
  writeln('Корень x равен ', res:0:4, ' количество итераций: n = ', n);
end.