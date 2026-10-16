import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# --- Carga inicial, se usa en todos los ejercicios ---
img_cv = cv2.imread("test_image.jpg")
img_cv_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
img_pil = Image.open("test_image.jpg")


def ejercicio_1():
    # Carga y despliegue con OpenCV, matplotlib y Pillow
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(img_cv_rgb); axs[0].set_title("OpenCV (RGB)"); axs[0].axis("off")
    axs[1].imshow(img_cv_rgb); axs[1].set_title("matplotlib"); axs[1].axis("off")
    axs[2].imshow(img_pil);    axs[2].set_title("Pillow");     axs[2].axis("off")
    plt.tight_layout()
    plt.show()


def ejercicio_2():
    # Tipo de dato y tamaño
    print("OpenCV -> dtype:", img_cv.dtype, "| shape (alto, ancho, canales):", img_cv.shape)
    print("Pillow -> modo:", img_pil.mode, "| tamaño (ancho, alto):", img_pil.size)


def ejercicio_3():
    # Mostrar la imagen en pantalla
    plt.figure(figsize=(5, 5))
    plt.imshow(img_cv_rgb)
    plt.title("Imagen original")
    plt.axis("off")
    plt.show()


def ejercicio_4():
    # Conversiones RGB->gris y RGB->HSV
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)

    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(img_cv_rgb);            axs[0].set_title("RGB");              axs[0].axis("off")
    axs[1].imshow(img_gray, cmap="gray"); axs[1].set_title("Escala de grises"); axs[1].axis("off")
    axs[2].imshow(img_hsv);               axs[2].set_title("HSV");              axs[2].axis("off")
    plt.tight_layout()
    plt.show()


def ejercicio_5():
    # Histograma de intensidades en escala de grises
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    plt.figure(figsize=(6, 4))
    plt.hist(img_gray.ravel(), bins=256, range=(0, 256), color="gray")
    plt.title("Histograma de intensidades")
    plt.xlabel("Intensidad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


def ejercicio_6():
    # Normalización de píxeles entre 0 y 1
    img_norm = img_cv_rgb.astype(np.float32) / 255.0
    print("Rango original:", img_cv_rgb.min(), "-", img_cv_rgb.max())
    print("Rango normalizado:", round(float(img_norm.min()), 3), "-", round(float(img_norm.max()), 3))


def ejercicio_7():
    # Reescalado (x5, /3) y rotación (45°, 90°, 180°)
    h, w = img_cv.shape[:2]

    img_up = cv2.resize(img_cv_rgb, (w * 5, h * 5), interpolation=cv2.INTER_LINEAR)
    img_down = cv2.resize(img_cv_rgb, (w // 3, h // 3), interpolation=cv2.INTER_AREA)

    def rotar(imagen, angulo):
        cx, cy = imagen.shape[1] // 2, imagen.shape[0] // 2
        M = cv2.getRotationMatrix2D((cx, cy), angulo, 1.0)
        return cv2.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))

    img_45 = rotar(img_cv_rgb, 45)
    img_90 = rotar(img_cv_rgb, 90)
    img_180 = rotar(img_cv_rgb, 180)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_up);   axs[0].set_title(f"x5 ({img_up.shape[1]}x{img_up.shape[0]})");     axs[0].axis("off")
    axs[1].imshow(img_down); axs[1].set_title(f"/3 ({img_down.shape[1]}x{img_down.shape[0]})"); axs[1].axis("off")
    plt.tight_layout()
    plt.show()

    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    for ax, im, t in zip(axs, [img_45, img_90, img_180], ["45°", "90°", "180°"]):
        ax.imshow(im); ax.set_title(t); ax.axis("off")
    plt.tight_layout()
    plt.show()

    print("Original:", (w, h))
    print("Aumentada x5:", (img_up.shape[1], img_up.shape[0]))
    print("Reducida /3:", (img_down.shape[1], img_down.shape[0]))


def menu():
    ejercicios = {
        "1": ejercicio_1,
        "2": ejercicio_2,
        "3": ejercicio_3,
        "4": ejercicio_4,
        "5": ejercicio_5,
        "6": ejercicio_6,
        "7": ejercicio_7,
    }

    while True:
        print("\nEscribe un número del 1 al 7")
        opcion = input("> ")

        if opcion in ejercicios:
            ejercicios[opcion]()
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()