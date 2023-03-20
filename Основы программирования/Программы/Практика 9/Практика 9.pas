Program Writeln_Chislo_00_Z_Or_Chislo_Z;
var
  z:integer;
procedure TwoDigitNumber(Y:integer);
var
  X:integer;
begin
  writeln('Числа в которых находится число Z');
  for X:= 10 to 99 do
    if (X div 10 = Y) or (X mod 10 = Y) then
    begin
      writeln(X);
    end;
    
  writeln('Числа делящиеся на число Z');
  for X:= 10 to 99 do
    if (X mod Y = 0) then
    begin
      writeln(X)
    end;
    end;
   
begin
   writeln('Введите число Z');
   readln(Z);
   TwoDigitNumber(Z);
    
end.