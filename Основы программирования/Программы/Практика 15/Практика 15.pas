program AM;
var
  a: array [1..10] of integer;
  i,index,chislo:integer;
begin
  for i:=1 to 10 do 
  begin
    a[i] := random(10,100);
  end;
  writeln('Массив с случйными значениями');
  writeln(a);
  
  writeln('Введите индекс массива');
  readln(index);
  
  while index > 9 do 
    begin
    writeln('Индекс находится за пределами массива');
    writeln('Введите другой индекс');
    readln(index);
    end;
  
  
  writeln('Введите двухзначное число');
  readln(chislo);
  
  while (chislo <= 10) or (chislo > 100) do 
    begin
    writeln('Неверно введено двухзначное число');
    writeln('Введите другое число');
    readln(chislo);
    end;

    a[index + 1] := chislo;
    writeln(a);
end.