// Candies.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
#include <iostream>
using namespace std;
int C = 10;
#include <string>
class Candies
{
public:
    Candies() {
        color = 0;
        machineStep = "";
        exercisable = 1;
    };
    Candies(int Color, const string& MachineStep) :color(Color), machineStep(MachineStep),
        exercisable(1) { }
    ~Candies() {
        cout << "color=" << color << endl; cout << "machineStep =" << machineStep << endl;
    };
    //friend int endcolor(int, string);
    string machineStep;
    int exercisable;
private:
    int color;
    friend class Machine;
};
class Machine
{
public:
    Machine() { number = "999"; for (int i = 0; i < C; i++)colors[i] = 0; };
    Machine(const string& Num) :number(Num) {}
    Machine(int num, istream& input) {
           for (int i = 0; i < C; i++)colors[i] = 0;
           number = num;
           int i = 0, j = 0;
           while (1)
           {
               cin >> i >> j;
               if (getchar() == 'q') break;
               colors[i] = j;
           }
       }
    void createMachine(string& num, istream& input) {
        {
            for (int i = 0; i < C; i++)colors[i] = 0;
            number = num;
            int i = 0, j = 0;
            while (1)
            {
                cin >> i >> j;
                if (i ==-1 ) break;
                colors[i] = j;
            }
        }
    }
    void Change(Candies*);
    void Convert(Candies*);
    //~Machine() = default;
    ~Machine() {
        cout << "Machine number is " << number << endl;
        for (int i = 0; i < C; i++)
        {
            cout << "colors[" << i << "]=" << colors[i] << endl;
        }
    };
    string number;
private:
    int* colors = new int[C];
};
void Machine::Change(Candies* candies) {
    if (colors[candies->color] != 0)
    {
        candies->color = colors[candies->color];
        candies->machineStep = candies->machineStep + number;
    }
}
void Machine::Convert(Candies* candies) {
    string mechinecolornumber;//this machine can change color number
    mechinecolornumber = candies->machineStep[0];
    int ColorNumber = stoi(mechinecolornumber);
    int num = stoi(number);
    if ((ColorNumber == num) && (candies->exercisable = 1)) {
        if (colors[ColorNumber] != 0) {
            candies->color = colors[candies->color];

        }
        else
        {
            candies->exercisable = 0;
        }
    }
}

int main()
{
    //cin >> C;
    Candies c(0, "123");
   /* Machine T1(1, cin);
    Machine T2(2, cin);
    Machine *T[10];
    T[1] = &T1;
    T[2] = &T2;*/
    Machine T[10];
    int i = 0;
    while (1)
    {
        cin >> i;
        if (i <= 10)
        {
            string k;
            k = to_string(i);
            cout << k;
            T[i].createMachine(k, cin);
        }
        else {
            break;
        }
    }
    //while ()
    //{
    for (int i = 0; i<3; i++) {
        string machibemap;
        machibemap = c.machineStep[i];

        int Machinemap = stoi(machibemap);
        cout << Machinemap<<endl;
        T[Machinemap].Convert(&c);
    }
   // }




}
