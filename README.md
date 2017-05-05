# laboratorium
//Zadanie2.
//Czy podany graf jest eulerowski?
//Kolejnosc wierzcholk�w umieszczanych w grafie ma znaczenie.
//Autor: Bartlomiej Pysiak, nr indeksu 251191
#include <stack>
#include <vector>
#include <iostream>
#define MAKS 500
using namespace std;
bool tu_bylem[MAKS];
vector<int> graf[MAKS];
vector<int> wynik;
int byc[MAKS][MAKS];
int wypisz_cykl(int v) //funckaj wrzuca na vector wynik kolejne przejscia drzewa graf
{
    while(!graf[v].empty())
    {
        int w = graf[v].back();
        graf[v].pop_back();
        if(byc[v][w]==0)
        {
            byc[v][w]=1;
            byc[w][v]=1;
            wypisz_cykl(w);
            wynik.push_back(w);
        }
    }
}
int main()
{
    int ile_w,ile_kr,i,v1,v2;
    bool czy_spojny;
    stack<int>stos;
    cout<<"PROGRAM ZWRACAJACY INFORMACJE CZY PODANY PRZEZ UZYTKOWNIKA GRAF JEST EULEROWSKI.\n";
    cout<<"-------------------------------------------------------------------------------\n";
    cout << "WCZYTAJ LICZBE WIERZCHOLKOW I KRAWEDZI GRAFU (SEPARATOR-SPACJA).\n";
    cin>>ile_w>>ile_kr;
    int tab[ile_w];
    for(i=0; i<ile_w; i++) {
    cout<<"ILE KRAWEDZI MA WIERZCHOLEK " <<i<< ": ";
    cin>>tab[i];
    }
    cout<<"\nWCZYTAJ WIERZCHOLEK (SPACJA) WIERZCHOLEK.\n";
    for(i=0; i<2*ile_kr; i++)
    {
        cin>>v1>>v2;
        graf[v1].push_back(v2);
    }
    for(i=0; i<ile_w; i++)
    {
        cout<<"\n"<<i<<" LACZY SIE Z: ";
        for(int j=0 ;j<graf[i].size(); j++)
            cout<<graf[i][j]<<", ";
    }
    cout<<endl;
    stos.push(0);
    while(!stos.empty())
    {
        v1=stos.top();
        stos.pop();
        if(!tu_bylem[v1])
        {
            tu_bylem[v1]=true;
            for(int i=0; i<graf[v1].size(); i++)
                if(!tu_bylem[graf[v1][i]])
                    stos.push(graf[v1][i]);
        }
    }
    czy_spojny=true;
    for(i=0; i<ile_w; i++) //jezeli nie wszystkie wierzcholki odwiedzone -> graf niespojny
        if(!tu_bylem[i])
        {
            czy_spojny=false;
            cout<<"\nNIE SPOJNY, WIEC TEZ NIE EULEROWSKI\n";
            return 0;
        }
    cout<<endl;
    (czy_spojny && ile_kr%2==0) ? cout<<"\nEULEROWSKI.\n" : cout<<"\nSPOJNY, ALE NIE EULEROWSKI.\n"; //warunek eulerowskiego grafu
    wypisz_cykl(v2);
    if(czy_spojny && ile_kr%2==0)
    {
        cout<<"\nCYKL EULERA: ";
        int pr_ost = wynik.back(); //pierwszy->ostatni, dopisuje na koncu petli wierzcholek od ktorego zaczynal sie cykl
        for(int i=0; i<ile_kr; i++)
        {
            cout << wynik.back() << " --> "; //wypisuje ostatni element stosu
            wynik.pop_back(); //zdejmuje ostatni element ze stosu
        }
        cout<<pr_ost;
    }
    cout<<endl;
    return 0;
}
