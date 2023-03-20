Program Massiv_9_znah;
var
  a:array [1..8] of integer;
  i:integer;
  res,sum:real;
begin
  for i:= 1 to 8 do
  begin
    a[i] := 2 * i;
    writeln('Число ', i, ' ' ,a[i]);
    end
end.