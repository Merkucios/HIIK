program Вывод_чисел_от1_до5_в_обр_порядке;
var chislo:integer;
begin
  for chislo := 5 downto 1 do
  begin
    case chislo of
    5: writeln('Пять');
    4: writeln('Четыре');
    3: writeln('Три');
    2: writeln('Два');
    1: writeln('Один');
    end;
  end;
end.