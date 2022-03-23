from PIL import Image

img= Image.open("/home/max/Imagens/Max1.jpg")   #Aqui voce coloca caminho para abrir a imagem
blackAndWhite = img.convert("L")
blackAndWhite.save("/home/max/ImagensMax1.jpg")  #Aqui voce coloca caminho para Salvar a imagem
blackAndWhite.show()