#include <iostream>
#include <algorithm>

// Функция для сортировки массива методом простого выбора
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[i], arr[min_idx]);
    }
}

int main() {
    setlocale(LC_ALL, "RU");
    const int n = 10;
    std::cout << "Размер массива = 10 " << std::endl;

    int A[n];
    std::cout << "Введите элементы массива A: ";
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    int B[n]; // массив B, в который будут скопированы элементы из A
    int b_size = 0; // размер массива B

    for (int i = 0; i < n; i += 2) {
        if (A[i] % 2 == 0) {
            B[b_size++] = A[i];
        }
    }

    // Сортировка массива B методом простого выбора
    selectionSort(B, b_size);

    std::cout << "Массив B после сортировки: ";
    for (int i = 0; i < b_size; i++) {
        std::cout << B[i] << " ";
    }

    return 0;
}
