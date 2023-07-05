#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX_SIZE = 100;

#pragma region Идентификатор процедур
void A1(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            arr[i] *= 2;
        }
        cout << arr[i] << " ";
    }
    cout << endl;
}


void A2(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 != 0) {
            arr[i] += 10;
        }
        cout << arr[i] << " ";
    }
    cout << endl;
}

void A3(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        if (arr[i + 1] % 2 == 1) {
            for (int j = i + 1; j < size; j++) {
                arr[j] = 0;
            }
            break;
        }
    }
    // вывод результата на консоль
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void A4(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        if (arr[i + 1] % 2 == 0) {
            for (int j = i + 1; j < size; j++) {
                arr[j] -= 2;
            }
            break;
        }
    }
    // вывод результата на консоль
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
void A5(int arr[], int size) {
    for (int i = 1; i < size - 1; i += 2) {
        if (arr[i] % 2 == 1 && arr[i - 1] % 2 == 0 && arr[i + 1] % 2 == 0) {
            arr[i - 1] /= 2;
            arr[i + 1] /= 2;
        }
    }

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;


}

void C1(int arr[], int size) {
    int start_index = -1, end_index = -1, max_length = 0, curr_length = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            if (curr_length == 0) {
                start_index = i;
            }
            curr_length++;
        }
        else {
            if (curr_length > max_length) {
                max_length = curr_length;
                end_index = i - 1;
            }
            curr_length = 0;
        }
    }
    if (curr_length > max_length) {
        max_length = curr_length;
        end_index = size - 1;
    }
    if (max_length > 0) {
        for (int i = start_index; i <= end_index; i++) {
            arr[i] = arr[end_index + 1 + i - start_index - max_length];
        }
        size -= max_length;
    }

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void C2(int A[], int n) {
    int i = 0;
    while (i < n) {
        if (A[i] % 2 == 0) {
            int j = i;
            while (j < n && A[j] % 2 == 0) {
                j++;
            }
            if (j - i < 3) {
                for (int k = i; k < j; k++) {
                    A[k] = A[j];
                }
                n -= j - i;
            }
            else {
                i = j;
            }
        }
        else {
            i++;
        }
    }
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
}

void C3(int arr[], int size) {
    int i = 0;
    while (i < size) {
        if (arr[i] % 2 == 1) {
            int j = i + 1;
            while (j < size && arr[j] % 2 == 1) {
                j++;
            }
            if (j - i < 3) {
                for (int k = i; k < j; k++) {
                    cout << "Удаляем элемент " << arr[k] << endl;
                }
                for (int k = j; k < size; k++) {
                    arr[k - (j - i)] = arr[k];
                }
                size -= j - i;
            }
            else {
                i = j;
            }
        }
        else {
            i++;
        }
    }
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void C4(int arr[], int& size) {
    int counts[MAX_SIZE] = { 0 };
    for (int i = 0; i < size; i++) {
        counts[arr[i]]++;
    }
    for (int i = 0; i < size; i++) {
        if (counts[arr[i]] >= 2) {
            counts[arr[i]]--;
            int j = i + 1;
            while (j < size && counts[arr[i]] >= 1) {
                if (arr[j] == arr[i]) {
                    counts[arr[i]]--;
                }
                j++;
            }
            if (counts[arr[i]] >= 1) {
                for (int k = i; k < size - 1; k++) {
                    arr[k] = arr[k + 1];
                }
                size--;
                i--;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void C5(vector<int> arr) {
    std::vector<int> result;

    int i = 0;
    while (i < arr.size()) {
        // если текущий элемент нечетный, то добавляем его в результат и переходим к следующему
        if (arr[i] % 2 != 0) {
            result.push_back(arr[i]);
            i++;
        }
        else {
            // иначе ищем минимальный четный элемент в цепочке и удаляем его
            int j = i;
            int min_even = arr[j];
            while (j < arr.size() && arr[j] % 2 == 0) {
                min_even = std::min(min_even, arr[j]);
                j++;
            }
            result.push_back(min_even);
            i = j;
        }
        
        for (int x : result) {
            std::cout << x << " ";
        }
        std::cout << std::endl;
    }
}



#pragma endregion


int main()
{   
    setlocale(LC_ALL, "RU");
    std::vector<int> arrVec = { 3, 6, 4, 5, 2, 3, 4, 6, 4 };
    int arr[] = { 4, 2, 4, 2, 1, 2, 4, 6 };
    int size = 8;

    cout << "***** Задание А1 ***** \n";
    A1(arr, size);
    cout << "***** Задание А2 ***** \n";
    A2(arr, size);
    cout << "***** Задание А3 ***** \n";
    A3(arr, size);
    cout << "***** Задание А4 ***** \n";
    A4(arr, size);
    cout << "***** Задание А5 ***** \n";
    A5(arr, size);
    cout << "***** Задание C1 ***** \n";
    int arr1[] = { 4, 1, 9, 2, 2, 2, -1, 3 };
    C1(arr1, size);
    cout << "***** Задание C2 ***** \n";
    int arr2[] = { 13, 1, 34, 2, 51, 22, 34, 16 };
    C2(arr2, size);
    cout << "***** Задание C3 ***** \n";
    int arr3[] = { 4, 15, 41, 23, 1, -2, 34, 6 };
    C3(arr3, size);
    cout << "***** Задание C4 ***** \n";
    int arr4[] = { 4, 2, 3, -2, 1, 26, 44, 26 };
    C4(arr4, size);
    cout << "***** Задание C5 ***** \n";
    C5(arrVec);

    return 0;
}

