program Сумма_от6_до10;
var
  i,res,otnyat:integer;
begin
  i:=6; res := 0;
  repeat
    writeln('Введите отнимаемое число: ');
    readln(otnyat);
    writeln();
    res := res + i - otnyat;
    writeln('Сумма чисел равна: ' + res);
    i := i + 1;
  until i >= 10;
end.