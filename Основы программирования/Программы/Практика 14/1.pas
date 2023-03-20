program MA;
var
  a: array [1..20] of integer;
  i,j,res:integer;
begin
  res := 1;
  for i:= 1 to 20 do
  begin
    a[i] := random(-5,5);
    writeln('Индекс ', i, ' ', 'Число ', ' * ' , a[i], ' * ');
  end;
  
  for j:=1 to 20 do
  begin
    if (a[j] > 0) then begin
      writeln('Положительное значение в индексе ', j);
      res := res * a[j];
    end;
  end;
  writeln('Произведение ненулевых элементов равно ', res);
end.