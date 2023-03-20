program Разность_между_трёхзначными_числами_и_произведение_цифр_max_числа;
var A, B, Difference, CompositionOfNumbers:integer;
begin
  writeln('Введите первое трёхзначное число');
  readln(A);
  writeln('Введите второе трёхзначное число');
  readln(B);
  if (A div 100 <> 0) and (B div 100 <> 0) then begin
   if A > B then begin
    writeln('Максимальное число равно: ' + A);
    Difference := A - B;
    CompositionOfNumbers := (A mod 10) * (A div 10 mod 10) * (A div 100);
    end
  else begin
    writeln('Максимальное число равно: ' + B);
    Difference := B - A;
    CompositionOfNumbers := (B mod 10) * (B div 10 mod 10) * (B div 100);
  end;
  writeln('Разность чисел составила: ' + Difference);
  writeln('Произведение цифр максимального числа: ' + CompositionOfNumbers);
  end
  else begin
    writeln('Неправильно введены трёхзначные числа');
  end;
end. 
  