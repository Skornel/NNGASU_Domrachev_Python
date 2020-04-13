#include <iostream>
#include <vector>
#include <fstream>

using namespace std;
int n=4, m=4;
int maximum = 0;
int minimum = 100;

vector <vector<int>> vvod_dannyx(int n, int m)
{
    ifstream in("C:\\Courses\\Cpp\\input.txt");
    vector < vector <int> > a(n, vector <int>(m));
    if (in.is_open())
    {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                {
                    in >> a[i][j];
                }
            in.close();
            
    }
    return a;
}
void raschet(vector < vector <int> > a) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] >= maximum)
            {
                maximum = a[i][j];

            };
        }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] <= minimum)
            {
                minimum = a[i][j];

            };
        }
}
void vyvod_resultata(int max, int min) {
    ofstream out;
    out.open("C:\\Courses\\Cpp\\output.txt");
    out << "Max is " << max << " Min is " << min << " difference is " << max - min;
    out.close();
}
int main() {
    raschet(vvod_dannyx(n, m));
    vyvod_resultata(maximum, minimum);
    return 0;
}