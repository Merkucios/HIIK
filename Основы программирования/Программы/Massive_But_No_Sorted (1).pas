Program F;

procedure Vvod(var b:array of integer);
var
  x:integer;
begin
  writeln('������� ����� ��������� �������');
  readln(x);
  SetLength(b,x);
  writeln();
end;

procedure Vivod(var c:array of integer);
var
  x,i:integer;
begin
  x := Length(c);
  writeln('���������� ����� �������');
  for i:=0 to x-1 do
  begin
    write(c[i] , ' ');
  end;
  writeln();
end;


procedure Vvod_Clava(); // 1
var
  a:array of integer;
  i,j,x:integer;
begin
  Vvod(a);
  writeln('���� � ����������');
  writeln('*��������� ������ � ����������*');
  x := Length(a);
  for i:= 0 to x-1 do
  begin
    readln(a[i]);
  end;
  
  Vivod(a);
end;

procedure Random(); // 2
var
  f:array of integer;
  i,j,x:integer;
begin
  Vvod(f);
  writeln('*��������� ������ ���������� ����������*');
  x := Length(f);
  for i:= 0 to x-1 do
  begin
    f[i] := random(-100,130);
  end;
  Vivod(f);
end;

procedure IndexX2(); // 3
var
  f:array of integer;
  i,j,x:integer;
begin
  Vvod(f);
  x := Length(f);
  for i:= 0 to x-1 do
  begin
    f[i] := i * 2
  end;
  
  Vivod(f);
end;

begin
  Vvod_Clava();
  writeln();
  Random();
  writeln();
  IndexX2();
end.

