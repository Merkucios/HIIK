Program F;

var
  a: array [1..9] of integer;
  i,j,index,max:integer;
begin
  for i:=1 to 9 do begin
    writeln('Введите число массива'); 
    readln(a[i]);
    if (a[i] > 100) and (a[i] < 1000) then
    begin
      writeln(i, ' ', a[i]);
    end
    else
    begin
      a[i] := 0;
    end;
  end;
  writeln(a);
  
  max := a[1];
  for j:=1 to 9 do begin
    if a[j] > max then begin
      index := j;
      max:= a[j];
    end;
  end;
  writeln('Максимум массива в индексе ' , index);
  
  max := (max div 100) + (max div 10 mod 10) + (max mod 10);
  writeln('Сумма цифр маскимального числа', ' ', max);
end.