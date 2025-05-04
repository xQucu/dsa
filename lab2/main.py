from PIL import Image
import numpy as np
from collections import Counter
import time


def main() -> None:
    grayScaleArray = yodaThresholdAndReturnGrayScale()
    grayScaleImg = Image.fromarray(grayScaleArray)
    grayScaleImg.save("grayScaleYoda.jpg")
    enhanceContrast(grayScaleArray)
    meanDP()
    meanNDP()


def meanDP() -> None:
    im = Image.open("road.jpg")
    imageArray = np.array(im)
    grayScaleArray = np.zeros(
        (imageArray.shape[0], imageArray.shape[1]), dtype=np.uint8)

    for i, pixelRow in enumerate(imageArray):
        for j, pixel in enumerate(pixelRow):
            mean = np.mean(pixel)
            grayScaleArray[i][j] = mean

    startTime = time.time()

    maskSize = 71
    height, width = grayScaleArray.shape
    summedAreaTable = np.zeros((height+1, width+1), dtype=np.float64)

    blurredImgArray = np.zeros_like(grayScaleArray)

    for i in range(height):
        for j in range(width):
            summedAreaTable[i+1, j+1] = (grayScaleArray[i, j] + summedAreaTable[i,
                                         j+1] + summedAreaTable[i+1, j] - summedAreaTable[i, j])

    for i in range(height - maskSize + 1):
        for j in range(width - maskSize + 1):
            windowSum = (summedAreaTable[i+maskSize, j+maskSize] - summedAreaTable[i,
                         j+maskSize] - summedAreaTable[i+maskSize, j] + summedAreaTable[i, j])

            mean = windowSum / (maskSize * maskSize)
            blurredImgArray[i, j] = mean

    elapsedTime = time.time() - startTime
    minutes = int(elapsedTime // 60)
    seconds = int(elapsedTime % 60)

    blurredImg = Image.fromarray(blurredImgArray)
    blurredImg.save(f"blurredImageDP_{minutes}m_{seconds}s.jpg")


def meanNDP() -> None:
    im = Image.open("road.jpg")
    imageArray = np.array(im)
    grayScaleArray = np.zeros(
        (imageArray.shape[0], imageArray.shape[1]), dtype=np.uint8)

    for i, pixelRow in enumerate(imageArray):
        for j, pixel in enumerate(pixelRow):
            mean = np.mean(pixel)
            grayScaleArray[i][j] = mean

    startTime = time.time()

    for i, pixelRow in enumerate(imageArray[:-71]):
        for j, pixel in enumerate(pixelRow[:-71]):
            total = 0
            for x in range(71):
                for y in range(71):
                    total += np.mean(imageArray[i + x][j + y])
            mean = total / (71 * 71)
            grayScaleArray[i][j] = mean

    elapsedTime = time.time() - startTime
    minutes = int(elapsedTime // 60)
    seconds = int(elapsedTime % 60)

    grayScaleImg = Image.fromarray(grayScaleArray)

    grayScaleImg.save(f"blurredImageNDP_{minutes}m_{seconds}s.jpg")


def enhanceContrast(grayScaleArray: np.ndarray) -> None:
    levels = Counter(grayScaleArray.flatten())
    total = levels.total()
    cumulativeHistogram = np.zeros(256)
    currentSum = 0
    for i in range(256):
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
