Program HeightOfTriangle;
var a,b,c:integer;
    p,ha,hb,hc:real;
begin
  writeln('Введите значения сторон треугольника'); // Аннотация
  readln(a,b,c);
  p := (a+b+c) / 2;
  // Блок формул высоты
  ha := 2/a * Sqrt(p * (p-a) * (p-b) * (p-c)); 
  hb := 2/b * Sqrt(p * (p-a) * (p-b) * (p-c));
  hc := 2/c * Sqrt(p * (p-a) * (p-b) * (p-c));
  // Результат
  writeln('Высота треугольника по высоте а: ', ha:1:1);
  writeln('Высота треугольника по высоте b: ', hb:1:1);
  writeln('Высота треугольника по высоте c: ', hc:1:1);
end.