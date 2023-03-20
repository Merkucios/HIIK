program AM;
var
  a: array [1..10] of integer;
  i,j,chislo:integer;
begin
  for i:=1 to 10 do 
    begin
    writeln('Введите число массива'); 
    readln(a[i]);
    end;
  writeln();
  writeln('Массив из введённых чисел');
  writeln(a);
  
  writeln('Введите удаляемое число массива');
  readln(chislo);
  
  for j:=1 to 10 do
  begin
    if a[j] = chislo then
    begin
      a[j] := 0
    end
    else
    begin
      continue;
    end;
  end;
  writeln('Полученный массив');
  writeln(a);
end.