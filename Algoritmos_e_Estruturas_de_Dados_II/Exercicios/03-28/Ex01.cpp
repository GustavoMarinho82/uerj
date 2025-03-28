#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct MuroInfinito {
	int e;
	MuroInfinito* Ant;
	MuroInfinito* Prox;
};

void insere_muro(MuroInfinito** L, int x) {
	MuroInfinito* No = (MuroInfinito*) malloc(sizeof(MuroInfinito));
	No->e = x;
	
	if (*L == NULL) {
		No->Prox = No;
		No->Ant = No;
	
	} else {
		No->Ant = (*L)->Ant;
		No->Prox = *L;
		(*L)->Ant->Prox = No;
		(*L)->Ant = No;
		
	}
	
	(*L) = No;
}

void imprimir_muro(MuroInfinito* L) {
	if (L != NULL) {
		MuroInfinito* p = L;
		
		printf("%d", p->e);
		p = p->Prox;
		
		while (p != L) {
			printf(" - %d", p->e);
			p = p->Prox;
		}
	}
	
	printf("\n");
}

MuroInfinito* construir_muro(int tamanho) {
	MuroInfinito* L = NULL;
	
	for (int i = 0; i < tamanho; i++)
		insere_muro(&L, i);
		
	return L;
}

int busca_dupla(MuroInfinito* L, int elemento, int pos_inicial) {
	//returna a distancia do numero encontrado com a pósição inicial
	while (pos_inicial-- > 0)
		L = L->Prox;
		
	if (L->e == elemento) {
		return 0
	}
}

int main() {
	MuroInfinito* L = construir_muro(10);
	
	imprimir_muro(L);
	
	busca_dupla(L, )
	
	return 0;
}
