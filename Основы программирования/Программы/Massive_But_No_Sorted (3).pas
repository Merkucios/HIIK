Program Massiv_9_znah;
var
  a:array [1..15] of integer;
  i:integer;
  res,sum:real;
begin
  writeln('Числа массива');
  for i:= 1 to 15 do
  begin
    a[i] := random(-10,10);
    writeln(i , ' ', a[i]);
    if i mod 2 <> 0 then begin
    sum := a[i] + sum;
    end;
    end;
    writeln('Сумма ',sum);
end.