#include <stdio.h>
#include <math.h>

int somar_salarios_2a2(int*, int);

int main() {
    int tamanho = 5;
    int salarios[] = {2000, 1500, 4000, 1200, 1};

    printf("Soma dos Salários: %d\n", somar_salarios_2a2(salarios, tamanho));

    return 0;
}

int somar_salarios_2a2(int* salarios, int tamanho) {
    int salarios_aux[tamanho];

    for (int i = 0; i < tamanho; i++) //Copia o conteúdo de salarios para o vetor auxiliar
        salarios_aux[i] = salarios[i]; 

    while (tamanho > 1) {
        for (int i = 0, j = 0; i <= tamanho/2; i++, j += 2)
        	salarios_aux[i] = salarios_aux[j] + ((j + 1 < tamanho) ? salarios_aux[j + 1] : 0);

        tamanho = ceil(tamanho/2.0);
    }

    return salarios_aux[0];
}