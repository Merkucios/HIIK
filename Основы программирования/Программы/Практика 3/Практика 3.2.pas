Program Значения;
const symbol = '*'; // Символ звёздчка как разграничитель 
var
  A, B:real;
  R:integer;
  begin
    R := 12;
    writeln(symbol * R);
    writeln('Введите число A');
    readln(A);                    // Ввод числа A
    writeln(symbol * R);
    writeln('Введите число B');
    readln(B);                    // Ввод числа B
    writeln(symbol * R);
    
    // Аннотация пользователю о производимых арифметических операциях
    writeln(symbol + 'A*B' + symbol + 'A+B' + symbol + 'A-B' + symbol + 'A/B' + symbol); 
    write(symbol);
    // Вывод арифметических операций
    write(A*B);
    write(symbol);
    write(A+B);
    write(symbol);
    write(A-B);
    write(symbol);
    write(A/B:1:1); 
    write(symbol);
  end.