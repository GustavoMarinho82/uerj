//EM PRODUÇÃO
use std::io;

fn main() {
    let mut vetor1: [i32; 5] = [0; 5];
    let mut vetor2: [i32; 5] = [0; 5];
    let mut vetor_intersecao [i32; 5] = [0; 5];
    
    for i in 0..5 {
        vetor1[i] = ler_i32(format!("Digite um valor para o Vetor 01 na coordenada {}", i));
        vetor2[i] = ler_i32(format!("Digite um valor para o Vetor 02 na coordenada {}", i));
    }
    
    for x in vetor1 {
        for (x in vetor2) and !(x in vetor_intersecao) {
            d
        }
    }
    println!("{:?} \n{:?}", vetor1, vetor2);
}

fn ler_i32(texto: String) -> i32 {
    println!("{}", texto);
    
    let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Erro ao ler a linha!");
    
    input.trim().parse().expect("Erro ao converter o input")
}
