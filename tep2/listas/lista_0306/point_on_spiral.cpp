#include <bits/stdc++.h>

using namespace std;

int main() {
    int x, y;
    int tipo = 1; // x = 0, y = 1
    int encontrado = 0, passo = 0, procedimento, valor = 0;
    int intervalo[1000][2];
    intervalo[0][0] = 0; 
    intervalo[0][1] = 1;

    cin >> x >> y;

    while (!encontrado){
        // printf("Passo %d - Tipo %d - Valor %d - Intervalo %d : %d - Encontrado %d\n", passo, tipo, valor, intervalo[passo][0], intervalo[passo][1], encontrado);
        // cout << (tipo == 1) << (y == valor) << (x <= intervalo[passo][1]) << (x >= intervalo[passo][0]) << endl;
        if ((tipo == 1) && (y == valor) && (x >= intervalo[passo][0]) && (x <= intervalo[passo][1])){
            encontrado = 1;
        } else if ((tipo == 0) && (x == valor) && y >= (intervalo[passo][0])  && (y <= intervalo[passo][1])){
            encontrado = 1;
        }
        tipo = 1 - tipo;
        
        procedimento = passo%4;
        switch(procedimento){
            case 0:
                valor = abs(valor) + 1;
                intervalo[passo+1][0] = intervalo[passo][0];
                intervalo[passo+1][1] = intervalo[passo][1];
                break;
            case 1:
                intervalo[passo+1][0] = -intervalo[passo][1];
                intervalo[passo+1][1] = intervalo[passo][1];
                break;
            case 2:
                valor = - valor;
                intervalo[passo+1][0] = intervalo[passo][0];
                intervalo[passo+1][1] = intervalo[passo][1];
                break;
            default:
                intervalo[passo+1][0] = intervalo[passo][0];
                intervalo[passo+1][1] = intervalo[passo][1] + 1;
        }
        passo++;
    }

    cout << passo - 1 << endl;

    return 0;
}