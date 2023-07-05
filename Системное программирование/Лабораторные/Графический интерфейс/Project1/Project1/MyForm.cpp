#include "MyForm.h"

#include <Windows.h>

using namespace Project1;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
    // �������� ���������� �����
    MyForm^ form = gcnew MyForm();

    // ������������� ����
    HWND hWnd = (HWND)form->Handle.ToPointer();
    ShowWindow(hWnd, nShowCmd);

    // ������ ����� ���������
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // ������� ���� ������ �� ����������
    return (int)msg.wParam;
}