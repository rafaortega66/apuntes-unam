import cv2
import matplotlib.pyplot as plt
from PIL import Image

# 1. Carga con OpenCV (llega en BGR) y conversión a RGB para desplegar bien
img_cv = cv2.imread("test_image.jpg")
img_cv_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# 2. Carga con Pillow (ya en RGB de forma nativa)
img_pil = Image.open("test_image.jpg")

# 3. Desplegar las tres versiones
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(img_cv_rgb)
axs[0].set_title("OpenCV (convertido a RGB)")
axs[0].axis("off")

axs[1].imshow(img_cv_rgb)
axs[1].set_title("matplotlib")
axs[1].axis("off")

axs[2].imshow(img_pil)
axs[2].set_title("Pillow")
axs[2].axis("off")

plt.tight_layout()
plt.show()