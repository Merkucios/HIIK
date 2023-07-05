#include <iostream>
#include <math.h>

using namespace std;

const double G = 6.67e-11; // гравитационная постоянная, м^3/(кг*с^2)

// Функция для вычисления функции 1.1: x = 4y^2 / (sqrt(4z)-2t^3) при t = 1 ; z = 3; y = sin t
void func1_1() {
    double t = 1;
    double z = 3;
    double y = sin(t);
    double x = 4 * pow(y, 2) / (sqrt(4 * z) - 2 * pow(t, 3));
    cout << "1.1: x = " << x << endl;
}

// Функция для вычисления функции 1.2: сопротивление проводника по закону Ома
void func1_2(double U, double I) {
    double R = U / I;
    cout << "1.2: Сопротивление проводника: R = " << R << endl;
}

// Функция для вычисления функции 2.1: x = 4y^3 - z/t при t = 2; z = 3; y = cos(t+z)
void func2_1() {
    double t = 2;
    double z = 3;
    double y = cos(t + z);
    double x = 4 * pow(y, 3) - z / t;
    cout << "2.1: x = " << x << endl;
}

// Функция для вычисления функции 2.2: расстояние, пройденное телом1
void func2_2(double v0, double a, double t) {
    double s = v0 * t + 0.5 * a * pow(t, 2);
    cout << "2.2: Расстояние, пройденное телом1: s = " << s << endl;
}

// Функция для вычисления функции 3.1: x = 6t^2 - (z+1)/y^2 при y = 2; z = 4; t = sin(2+z)
void func3_1() {
    double y = 2;
    double z = 4;
    double t = sin(2 + z);
    double x = 6 * pow(t, 2) - (z + 1) / pow(y, 2);
    cout << "3.1: x = " << x << endl;
}

// Функция для вычисления функции 3.2: кинетическая энергия тела
void func3_2(double m, double v) {
    double T = 0.5 * m * pow(v, 2);
    cout << "3.2: Кинетическая энергия тела: T = " << T << endl;
}

// Функция 4.2
void func4_2() {
    double G = 6.67e-11; // Гравитационная постоянная
    double m1 = 7e22; // Масса Луны
    double m2 = 6e24; // Масса Земли
    double r_min = 356410e3; // Минимальное расстояние между Землей и Луной
    double r_max = 406700e3; // Максимальное расстояние между Землей и Луной

    // Вычисление силы притяжения в разных точках орбиты Луны
    double F_min = G * m1 * m2 / pow(r_min, 2);
    double F_max = G * m1 * m2 / pow(r_max, 2);

    cout << "4.2 Сила притяжения Луны к Земле на минимальном расстоянии: F = " << F_min << " Н" << endl;
    cout << "4.2 Сила притяжения Луны к Земле на максимальном расстоянии: F = " << F_max << " Н" << endl;
}

// Функция 4.1
void func4_1() {
    double z = 1;
    double t = 2;
    double y = t + z;
    double x = (8 * pow(z, 2) + 1) / (y + pow(t, 2));

    cout << "4.1 Результат функции x = " << x << endl;
}

// Функция 5.1
void func5_1() {
    double t = 3;
    double z = 1 / tan(t) + 2;
    double y = 4;
    double x = 8 * z / (exp(t) + 2) - pow(y, 2);
    cout << "5.1 x = " << x << endl;
}

void func5_2() {
    double m_earth = 6e24; // масса Земли, кг
    double v_earth = 30e3; // средняя скорость Земли на орбите, м/с
    double r_earth = 150e9; // среднее расстояние от Земли до Солнца, м

    // Расчет центробежной силы
    double F_centripetal = (m_earth * v_earth) / r_earth;

    std::cout << "5.2 Центробежная сила Земли: " << F_centripetal << " Н" << std::endl;
}

void func6_1() {
    double t = 1.0;
    double z = t + 2;
    double y = 4;
    double x = 8 * z / (exp(t) + 2) - pow(y, 2);
    std::cout << "6.1 x = " << x << std::endl;
}

void func6_2(double T) {
    double T1 = 27.0;
    double P1 = 75.0;
    double P2 = P1 * T / T1;
    std::cout << "6.2 P2 = " << P2 << " kPa" << std::endl;
}

void func7_1() {
    double y = 2.0;
    double t = 5.0 / (1 + pow(y, 2));
    double z = 4.0;
    double x = 2 * y + 3 * sqrt(t) - z;
    std::cout << "7.1 x = " << x << std::endl;
}


int main() {
    setlocale(LC_ALL, "RU");
    func1_1();
    func1_2(10,15);
    func2_1();
    func2_2(15, 3, 19);
    func3_1();
    func3_2(20, 15);
    func4_1();
    func4_2();
    func5_1();
    func5_2();
    func6_1();
    func6_2(30);
    func7_1();

    return 0;
}