Program Замена_Нулём;
var
  A,B:integer;
begin
  writeln('Введите два числа');
  readln(A,B);
  
  // Проверка чисел на равенство
  if A = B then begin
    A:= 0;
    B:= 0;
    end
    else begin
      // Проверка на наименьшее число A
      if A < B then begin
      A := 0;
      end;
      // Проверка на наименьшее число B
        if B < A then begin
        B := 0;
        end
    end;
  
  writeln('Полученный результат: ');
  writeln('Число A = ' + A);
  writeln('Число B = ' + B);
end.