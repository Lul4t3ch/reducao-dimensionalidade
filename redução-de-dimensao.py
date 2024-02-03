import cv2

def converter_para_cinza_e_binaria(imagem_path):
    # Carregar a imagem colorida
    imagem_colorida = cv2.imread(imagem_path)

    # Converter para níveis de cinza
    imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

    # Converter para imagem binarizada (preto e branco)
    _, imagem_binarizada = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

    # Mostrar as imagens
    cv2.imshow('Imagem em Níveis de Cinza', imagem_cinza)
    cv2.imshow('Imagem Binarizada', imagem_binarizada)

    # Aguardar por uma tecla e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho real da sua imagem
caminho_da_imagem = './profile.jpg'
converter_para_cinza_e_binaria(caminho_da_imagem)
