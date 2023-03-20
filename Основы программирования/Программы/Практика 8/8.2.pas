program Вывод_на_экран_всех_простых_чисел_меньших_K;
var
  k,chislo:integer;
begin
  writeln('Введите предел чисел');
  readln(k);
  chislo := 0;
  repeat
    if (chislo div 1 = chislo) and (chislo div chislo = 1) then begin
      writeln(chislo);
    end;
  until chislo >= k;
end.