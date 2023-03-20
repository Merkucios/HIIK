Program SquareOfRectangle;
var a,b, Square:integer;
    
begin
  writeln('Введите стороны прямоугольника');
  readln(a,b);
  Square := a * b;
  writeln('Площадь прямоугольника равна: ', Square);
  writeln('Нажмите ENTER чтобы закрыть программу');
  readln;
end.