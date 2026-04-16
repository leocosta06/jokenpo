package main

import "fmt"
// Função começando com letra minúscula:
// Função é PRIVADA
// Função ela só pode ser utilizada no próprio pacote

// Função começando com letra MASUCULA:
// Função é Pública
// Função ela só pode ser utilizada no próprio
func main(){
	somaDosValos:= soma(42,13)
	//fmt.Println(soma(42,13))
	fmt.Println(somaDosValos)
	menos:= sub(42,13)
	fmt.Println(menos)
	nome1 ,nome2:=digaNome("leozin")
	fmt.Println(nome1,nome2)
}
func sub(x int,y int) int{
	return x-y
} 
func soma(x int,y int) int{
	return x+y
} 
//func digaNome(nome string) string{
	//return nome
	//} 
func digaNome(nome string) (string, string){
	return nome, nome
	} 