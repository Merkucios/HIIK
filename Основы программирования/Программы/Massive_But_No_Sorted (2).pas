Program Massiv_9_znah;
var
  a:array [1..8] of integer;
  i:integer;
  res,sum:real;
begin
  for i:= 1 to 8 do
  begin
    writeln('Введитe ' ,i , ' число');
    readln(a[i]);
    // Подсчёт суммы чисел массива
    sum:= sum + a[i];
  end;
  res := sum / 8;
  writeln(res);
end.