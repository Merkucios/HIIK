#include "MyForm.h"

#include <Windows.h>

using namespace Project1;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
    // Создание экземпляра формы
    MyForm^ form = gcnew MyForm();

    // Инициализация окна
    HWND hWnd = (HWND)form->Handle.ToPointer();
    ShowWindow(hWnd, nShowCmd);

    // Запуск цикла сообщений
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Возврат кода выхода из приложения
    return (int)msg.wParam;
}