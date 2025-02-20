import cv2
import os
from matplotlib import pyplot as plt


def image_to_gray(img_path):

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"File not found: {img_path}")

    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Unable to load image. Check the file format and path: {img_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def noise_reduction(image):

    denoised = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    return denoised


def black_white(image):

    th = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)
    return th


def preprocess_image(img):

    image = cv2.imread(img)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = image_to_gray(img)

    adaptive_threshold= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,10)
    # تقليل التشويش
    denoised = noise_reduction(adaptive_threshold)

    bw_image = black_white(denoised)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.title("Gray Image")
    plt.imshow(gray, cmap='gray')
    plt.axis("off")

    # عرض الصورة الثانية
    plt.subplot(2, 2, 2)
    plt.title("Denoised Image")
    plt.imshow(adaptive_threshold, cmap='gray')
    plt.axis("off")

    # عرض الصورة الثالثة
    plt.subplot(2, 2, 3)
    plt.title("Image 3")
    plt.imshow(denoised, cmap='gray')

    # عرض الشكل
    plt.tight_layout()
    plt.show()

    return denoised
