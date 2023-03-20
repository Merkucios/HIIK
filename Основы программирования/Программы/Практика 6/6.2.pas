Program Число_делимое_на_квадрат_цифр;
var
  chislo,num1,num2,summa:integer;
begin
  for chislo := 10 to 99 do
  begin
    num1 := chislo div 10;
    num2 := chislo mod 10;
    summa := sqr(num1) + sqr(num2);
    if (summa mod 13 = 0) then
    begin
      writeln('Число суммы квадратов цифр которого делится на 13 ',chislo);
    end;
  end;
end.