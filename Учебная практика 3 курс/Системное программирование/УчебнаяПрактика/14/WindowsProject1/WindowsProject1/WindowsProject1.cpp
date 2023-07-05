#pragma once
#include <windows.h>


namespace MyForms {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for MyForm
	/// </summary>

// Программный код, расположенный выше, создан средой Visual Studio
// автоматически, поэтому автором не приводится 

this->PerformLayout();
}
#pragma endregion
// Программа, позволяющая выбрать текст из двух вариантов, задать цвет
// и размер шрифта для этого текста на трех вкладках TabControl
// с использованием переключателей RadioButton private: System::
Void Form1_Load(System::Object^ sender, System::EventArgs^ e)
{
	// Создание третьей вкладки "программно":
	auto tabPage3 = gcnew System::Windows::Forms::TabPage(); tabPage3->UseVisualStyleBackColor = true;

	// Добавление третьей вкладки в существующий набор
	// вкладок tabControl1:
	this->tabControl1->Controls->Add(tabPage3);
	// Добавление переключателей 5 и 6 на третью вкладку: tabPage3->Controls->Add(this->radioButton5); tabPage3->Controls->Add(this->radioButton6);
	// Расположение переключателей 5 и 6:
	this->radioButton5->Location = System::Drawing::Point(20, 15); this->radioButton6->Location = System::Drawing::Point(20, 58); this->Text = "Какая улыбка вам ближе";
	// Задаем названия вкладок:
	tabControl1->TabPages[0]->Text = "Текст"; tabControl1->TabPages[1]->Text = "Цвет"; tabControl1->TabPages[2]->Text = "Размер";
	// Эта пара переключателей изменяет текст: radioButton1->Text =
	"Восхищенная, сочувственная,\nскромно-смущенная"; radioButton2->Text = "Нежная улыбка, ехидная, бес" + "стыжая,\nподленькая, снисходительная";
	// или
	// radioButton2->Text = "Нежная улыбка, бесстыжая," +
	// Environment::NewLine + "подленькая, снисходительная";
	// Эта пара переключателей изменяет цвет текста: radioButton3->Text = "Красный";
	radioButton4->Text = "Синий";
	// Эта пара переключателей изменяет размет шрифта: radioButton5->Text = "11 пунктов";
	radioButton6->Text = "13 пунктов"; label1->Text = radioButton1->Text;
}
private:	System::Void
	radioButton1_CheckedChanged(System::Object^ sender, System::EventArgs^ e)
{
	label1->Text = radioButton1->Text;
}
private:	System::Void
	radioButton2_CheckedChanged(System::Object^ sender, System::EventArgs^ e)
{
	label1->Text = radioButton2->Text;
}
private:	System::Void
	radioButton3_CheckedChanged(System::Object^ sender, System::EventArgs^ e)
{
	label1->ForeColor = Color::Red;
}
private:	System::Void
	radioButton4_CheckedChanged(System::Object^ sender, System::EventArgs^ e)
{
	label1->ForeColor = Color::Blue;
}
private:	System::Void
	radioButton5_CheckedChanged(System::Object^ sender, System::EventArgs^ e)
{
	label1->Font = gcnew System::Drawing::
		Font(label1->Font->Name, 11);
}
private:	System::Void
	radioButton6_CheckedChanged(System::Object^ sender,

		System::EventArgs^ e)
{
	label1->Font = gcnew System::Drawing::Font(label1->Font->Name, 13);
}
};
}
