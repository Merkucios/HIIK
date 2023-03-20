Program Chetnoe_chislo;
var
  chislo:integer;
begin
  for chislo := 10 to 30 do
  begin
    if chislo mod 2 = 0 then begin
      writeln('Чётное число равно: ' , chislo);
    end;
  end;
end.