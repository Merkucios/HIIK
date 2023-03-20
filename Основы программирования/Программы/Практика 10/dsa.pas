Program _60_90_Equal_Num;
var
  A,B,res:integer;                                 
  Function Equal_Num(A:integer): integer; 
  var
    n:integer;
  begin
    for A:=60 to 90 do
      if (A div 10 = A mod 10) then
      begin
        writeln(A);
        n := n + 1;
      end;
      writeln('Количество шагов', ' ' , n);
      end;
begin
  res := Equal_Num(A);
end.