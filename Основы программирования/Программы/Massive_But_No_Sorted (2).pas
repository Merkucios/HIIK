Program Massiv_9_znah;
var
  a:array [1..8] of integer;
  i:integer;
  res,sum:real;
begin
  for i:= 1 to 8 do
  begin
    writeln('������e ' ,i , ' �����');
    readln(a[i]);
    // ������� ����� ����� �������
    sum:= sum + a[i];
  end;
  res := sum / 8;
  writeln(res);
end.