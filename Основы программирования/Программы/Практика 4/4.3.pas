Program Вывод_Трёхзначных_Чисел_В_Порядке_Убывания;
var
  A,B,C:integer;
begin
  writeln('Введите три трёхзначных числа');
  readln(A,B,C);
  // Проверка чисел на трёхзначность
  if (A div 100 <> 0) and (B div 100 <> 0) and (C div 100 <> 0) then begin
    
    // Проверка на максимальное число A
    if (A > B) and (A > C) then begin
      write(A, ' ');
      if B > C then begin
        write(B, ' ' ,C);
      end
      else begin
        write(C,' ', B);
      end;
    end;
    
    // Проверка на максимальное число B
    if (B > A) and (B > C) then begin
      write(B, ' ');
      if A > C then begin
        write(A, ' ', C);
      end
      else begin
        write(C, ' ', A);
      end;
    end;
    
    // Проверка на максимальное число C
    if (C > A) and (C > B) then begin
      write(C, ' ');
      if A > B then begin
        write(A, ' ', B);
      end
      else begin
        write(B, ' ', A);
      end;
    end;
    
  end
  
  // Если неправильно ввели числа
  else begin
    writeln('Неправильно введены трёхзначные числа');
  end;
end.