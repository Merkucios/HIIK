Program Domik;
  
var symbol:char;
    R:integer;
begin
    R:= 12;
    writeln('Введите символ для построения дома');
    readln(symbol);
    writeln;
    writeln;
    writeln;
    writeln('            ' + symbol);
    writeln('        ' + symbol + '        ' + symbol);
    writeln('      ' + symbol + '            ' + symbol);
    writeln('      ' + symbol * R '           ');
end.