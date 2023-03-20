Program Power;
var U,R:integer;
    I:real;
begin
  writeln('Введите напряжение и сопротивление участка цепи');
  readln(U,R);
  I := U / R; // По формуле Ома получаем
  writeln('Полученная сила тока равна: ', I:1:1);
end.