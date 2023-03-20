program Вывол_чисел_между_4значного_числа;
var
  chislo,num1,num2,res:integer;
begin
  writeln('Введите число: ');
  readln(chislo);
  num1 := chislo div 100 mod 10;
  num2 := chislo div 10 mod 10;
  if num1 < num2 then begin
    for res:= num1 to num2 do
    begin
      writeln(res);
    end;
    writeln();
    writeln('Обратный порядок');
    for res:= num2 downto num1 do
    begin
      writeln(res);
    end;
  end
  
  else begin
    for res:= num1 downto num2 do
    begin
      writeln(res);
    end;
    writeln();
    writeln('Обратный порядок');
    for res:= num2 to num1 do
    begin
      writeln(res);
    end;
  end;
end.