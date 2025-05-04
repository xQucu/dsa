from PIL import Image
import numpy as np
from collections import Counter


def main() -> None:
    grayScaleArray = yodaThresholdAndReturnGrayScale()
    grayScaleImg=Image.fromarray(grayScaleArray)
    grayScaleImg.save("grayScaleYoda.jpg")
    enhanceContrast(grayScaleArray)


def enhanceContrast(grayScaleArray: np.ndarray) -> None:
    levels = Counter(grayScaleArray.flatten())
    total = levels.total()
    cumulativeHistogram = np.zeros(256)
    currentSum = 0
    for i in range(256):
        print(currentSum)
        currentSum += levels[i]
        cumulativeHistogram[i] = currentSum/total

    mapping = np.floor(255 * cumulativeHistogram).astype(np.uint8)
    
    enhancedArray = np.zeros_like(grayScaleArray)
    for i in range(grayScaleArray.shape[0]):
        for j in range(grayScaleArray.shape[1]):
            enhancedArray[i, j] = mapping[grayScaleArray[i, j]]
    
    enhancedImage = Image.fromarray(enhancedArray)
    enhancedImage.save("enhancedContrast.jpg")


def yodaThresholdAndReturnGrayScale() -> np.ndarray:
    im = Image.open("yoda.jpg")
    imageArray = np.array(im)
    grayScaleArray = np.zeros(
        (imageArray.shape[0], imageArray.shape[1]), dtype=np.uint8)
    singleThresholdImageArray = np.zeros(
        (imageArray.shape[0], imageArray.shape[1]), dtype=np.uint8)
    doubleThresholdImageArray = np.zeros(
        (imageArray.shape[0], imageArray.shape[1]), dtype=np.uint8)
    for i, pixelRow in enumerate(imageArray):
        for j, pixel in enumerate(pixelRow):
            mean = np.mean(pixel)
            grayScaleArray[i][j] = mean
            singleThresholdImageArray[i][j] = 0 if mean < 125 else 255
            doubleThresholdImageArray[i][j] = 0 if 85 <= mean <= 170 else 255

    singleThresholdImage = Image.fromarray(singleThresholdImageArray)
    singleThresholdImage.save("singleThresholdImage.jpg")

    doubleThresholdImage = Image.fromarray(doubleThresholdImageArray)
    doubleThresholdImage.save("doubleThresholdImage.jpg")
    return grayScaleArray


main()
