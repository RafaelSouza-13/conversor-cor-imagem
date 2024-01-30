from PIL import Image

class ConversorImagem():
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def converter_cinza(self):
        imagem = Image.open(self.path)
        pixels = imagem.load()

        for i in range(imagem.width):
            for j in range(imagem.height):
                r, g, b = pixels[i, j]
                cinza = int((r + g + b) / 3)
                pixels[i, j] = (cinza, cinza, cinza)

        self.imagem_cinza = imagem.save(f"{self.name}_cinza.png")
    
    def converte_preto_branco(self, limiar):
        if(self.imagem_cinza == None):
            self.converter_cinza()
        
        imagem = Image.open(f"{self.name}_cinza.png")
        pixels = imagem.load()

        for i in range(imagem.width):
            for j in range(imagem.height):
                r, g, b = pixels[i, j]
                cinza = int(r + g + b)
                if(cinza  > limiar):
                    pixels[i, j] = (255, 255, 255)
                else:
                    pixels[i, j] = (0, 0, 0)
        
        self.imagem_preto_branco = imagem.save(f"{self.name}_preto_branco.png")


    def exibe_imagem_cinza(self):
        if(self.converter_cinza):
            imagem = Image.open(f"{self.name}_cinza.png")
            imagem.show()
        else:
            raise Exception("Não há imagem convertida")
    
    def exibe_imagem_preto_branco(self):
        if(self.converter_cinza):
            imagem = Image.open(f"{self.name}_preto_branco.png")
            imagem.show()
        else:
            raise Exception("Não há imagem convertida")