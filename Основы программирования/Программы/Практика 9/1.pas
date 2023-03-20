Program Example;
var
A, N :integer; 
S :longint;
Procedure Degree (X, Y :integer; var St :longint); // Объявление процедуры, вычисляющая степень целого числа
  var                                              // Внутренние переменые процедуры
    i :integer;                                    // Итератор цикла
  begin                                            // Тело процедуры
    St := 1;                                       // St - число в степени , Y - степень, X - Число
    For i := 1 to Y do                            
      St := St * X;
    end;
    begin
    writeln ('Введите два числа');
    readln (A, N);                                  // Ввод параметров процедуры
    Degree (A, N, S);                               // Вычисление процедупы
    Writeln ('Результат = ', S);                    // Вывод результата
    Readln;
End.