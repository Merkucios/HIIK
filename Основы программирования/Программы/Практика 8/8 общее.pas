Program Test;
var 
    b, a: real;
    n: integer;
begin
  repeat
    write('Введите начальное приближение корня в интервале [2..3]: ');
    readln(a)
  until (2 <= a) and (a <= 3);
  n := 0;
  repeat
    b := a;
    a := // нужно формулу
    inc(n)
  until abs(b - a) < 1e-4; // Условие норм
  writeln('Корень: x = ', a :0:4, ', количество итераций: n = ', n); // пойдёт
end.