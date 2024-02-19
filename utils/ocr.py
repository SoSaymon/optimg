async def perform_ocr(image_path, language="pol"):
    import pytesseract
    from PIL import Image

    myconfig = r"--psm 6 --oem 3 -l " + language

    img = Image.open(image_path)

    text = pytesseract.image_to_string(img, config=myconfig)

    return text


if __name__ == "__main__":
    print(perform_ocr("../files/korona.png"))
