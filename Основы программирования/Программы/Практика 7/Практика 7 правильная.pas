program Koren;

var 
    n: integer;
    x,y: real;

begin
  write('Введите начальное приближение корня в интервале [0..0.85]: ');
  readln(x);
  
  while (0 > x) or (x > 0.85) do
    begin
    write('Введите начальное приближение корня в интервале [0..0.85] ');
    readln(x);
    end;
  n := 0;
  
  while abs(y - x) > 0.5e-4 do
    begin
    y := x;
    x := 1 / (y - 3 + sin(3.6 * y));
    n := n + 1;
    end;
  writeln('Корень: x = ', x:0:4, ', количество итераций: n = ', n);
end.