Program Domik;

var i,R,j,m,k:integer;
    symbol:char;
 
begin
  // Основание дома
  R := 12; 
  writeln('Введите символ для построения дома');
  readln(symbol);
  writeln;
  writeln;
  writeln;
  writeln;
  // Крыша дома
  writeln('          ' + symbol);  
  writeln('       ' + symbol + '      ' + symbol);
  writeln('     ' + symbol + '          ' + symbol);
  
  write('     ');
   // Вывод верхний части прямоугольника
   write(symbol * R);
   writeln;
   
  // Цикл для вывода "стен дома". Цикл отвечает за количество символов в стенки, первый цикл выводит отступ и символ. Второй цикл выводит символы в стенке.
  for i:=2 to R - 8 do
     begin
       write('     ' + symbol);
       for j:=2 to R-1 do
         write(' ');
         write('' + symbol);
         writeln;
     end;
     
  // Вывод нижнего основания прямоугольника 
  write('     ');
  write(symbol * R);
  writeln;;
 end.