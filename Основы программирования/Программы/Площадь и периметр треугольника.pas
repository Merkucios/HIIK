﻿Program SqrOfTriangle;
var y, S, P, d:real;
    a, b:integer;
begin
  writeln('Введите длины сторон треугольника и угол между ними'); // Аннотация
  readln(a,b,y); 
  // Формула нахождения площади
  S := 0.5 * a * b * Sin(y); 
  // Формула нахождения периметра, почему Sqr(a) и Sqr(b) выдают ошибку имени переменной
  P := Sqrt(a*a + b*b - 2 * b * a * Cos (y)) + b + a;
  writeln('Площадь треугольника равна: ' , S:1:1);
  writeln('Периметр треугольника равен: ' , P:1:1);
end.