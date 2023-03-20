Program Двузначные_Числа_Кратные_2_и_5_одновременно;
var chislo:integer;
begin
  writeln('Полученные кратные числа 2 и 5');
  while chislo < 99 do
  begin
    if (chislo mod 2 = 0) and (chislo mod 5 = 0) then
      begin
        write(' ');
        writeln(chislo);
      end;
      chislo := chislo + 1;
  end;
end.