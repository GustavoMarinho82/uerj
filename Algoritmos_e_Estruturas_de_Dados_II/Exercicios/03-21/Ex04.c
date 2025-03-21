#include <stdio.h>
#include <stdbool.h>

int buscar_muro(int*, int, int, int);

int main() {
    int muro[1000];
    for (int i = 0; i < 1000; i++)
        muro[i] = 0;

    muro[87] = 1;

    int pos_elemento = buscar_muro(muro, 1, 750, 1000);

    if (pos_elemento == -1)
        printf("O elemento não foi encontrado!");
    
    else
        printf("O elemento está na posição %d do muro", pos_elemento);

    return 0;
}

int buscar_muro(int* muro, int elemento, int pos_inicial, int tamanho) {
    int i = 0;
    
    while ((pos_inicial + i < tamanho) || (pos_inicial - i >= 0)) { //Executa caso seja possível andar pra esquerda ou pra direita
        if ((pos_inicial + i < tamanho) && (muro[pos_inicial + i] == elemento))
            return pos_inicial + i;
        
        if ((pos_inicial - i >= 0) && (muro[pos_inicial - i] == elemento))
            return pos_inicial - i;

        i++;
    }

    return -1;
}