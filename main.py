from conversor_imagem import ConversorImagem

name = input("Digite um nome para a imagem: ")
path = input("Digite o caminho onde a imagem esta localizada: ")
limiar  = input("Digite o ponto de divisão de escala entre branco e o preto: ")

imagem = ConversorImagem(name, path)
imagem.converter_cinza()
imagem.converte_preto_branco(limiar)
imagem.exibe_imagem_cinza()
imagem.exibe_imagem_preto_branco()