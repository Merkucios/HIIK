Program P;
var
  C1,C2:integer;                  // Два числа 
  Nd:integer;                     // Переменная вывода НОД
  Function Nod(A,B:integer): integer; // Описание функции с выводом значения int (НОД)
  var
    R:integer;
  begin
    while (A mod B) <> 0 do // Цикл проверки чисел на вычисление НОД
    begin
      R := A mod B; // Блок вычислений НОД
      A := B;
      B := R;
    end;
    Nod := B; // Переменная хранящее значение НОД
    end;
begin
    writeln('Введите два целых положительных числа'); // Аннотация
    readln(C1,C2); 
    Nd := Nod(C1,C2); // Присваивание переменной значения функции
    writeln('НОД чисел ',C1, ' и ',C2, ' это ', Nd);
  end.