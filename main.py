from core import Node # Ejemplo de uso
from core import render
import cv2,os 

if __name__ == "__main__":
    # creamos las carpetas si no estan creadas en img/input y img/output
    if not os.path.exists('img/input'):
        os.makedirs('img/input')
    if not os.path.exists('img/output'):
        os.makedirs('img/output')
    #imagen de fondo
    background_path = "img/input/calle.png"
    # Cargar la imagen de fondo
    canvas = cv2.imread(background_path, cv2.IMREAD_UNCHANGED)
    # Verificar que la imagen se haya cargado correctamente
    if canvas is None:
        raise FileNotFoundError("Imagen no encontrada")
    # Asegurarse de que la imagen tenga un canal alfa
    if canvas.shape[2] == 3:
        # Convertir la imagen a un formato con canal alfa
        canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2BGRA)
    # Crear un nodo padre
    personaje = Node.NodeImagens("img/input/character.png", (100, 100), scale=0.2)
    # Crear nodos hijos
    patineta = Node.NodeImagens("img/input/skateboard.png", (55, 230), scale=0.2, parent=personaje)
    # Crear nodos hijos
    fuego = Node.NodeImagens("img/input/fire.png", (170, 100), scale=0.6, parent=personaje)
    # Mover el personaje a una posición inicial con todo e hijos
    personaje.set_position(100, 400)
    # movemos al personaje en linea recta y creamos una imagen por cada movimiento
    for i in range(24*5):
        # Limpiar el canvas
        Node.NodeImagens.clear_canvas(canvas, background_path)
        # Mover el personaje y la patineta
        personaje.move(5, 0)
        # Mover el fuego aparte del personaje
        fuego.move(3, 0)
        # Dibujar los nodos en el canvas
        personaje.draw(canvas)
        # Guardar la imagen en disco
        Node.NodeImagens.save_image(canvas, f"img/output/frame_{i:03}.png")
        # Mostrar la imagen en pantalla
        # cv2.imshow("Canvas", canvas)
        # Esperar 100 ms
        # cv2.waitKey(100)
    # cv2.destroyAllWindows()
    
    # valores para la generacion del video
    input_dir = 'img/output/'  # Directorio de las imágenes
    output_file = 'video_salida.avi'  # Archivo de salida con el formato deseado
    img_format = 'png'  # Formato de las imágenes (por ejemplo, 'png', 'jpg')
    output_format = 'avi'  # Formato de salida del video (por ejemplo, 'mp4', 'avi')
    fps = 24  # Cuadros por segundo
    # video creado
    renderer = render.VideoRenderer(input_dir, output_file, img_format, output_format, fps)
    renderer.create_video_from_images()