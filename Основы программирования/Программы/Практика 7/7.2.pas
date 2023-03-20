program Положительное_число_равно_выходу;
var num1,num2,user:integer;
    logic:boolean;
begin
  logic := true;
  while logic = true do
  begin
    writeln('Введите два числа: ');
    readln(num1,num2);
    if (num1 > 0) or (num2 > 0) then
    begin
      writeln('Положительные числа ведут к закрытию программы');
      break;
    end
    else 
      begin
        writeln('Сумма чисел равна: ', num1+num2);
        writeln('Продолжить выполнение программы?');
        writeln('1 - Да');
        writeln('2 - Нет');
        readln(user);
        case user of
          1: logic := true;
          2: logic := false;
          else writeln('Неправильно введена функция');
          break;          
        end;
      end;
   end;
end.