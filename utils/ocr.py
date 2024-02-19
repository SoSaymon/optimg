async def perform_ocr(image, language="pol"):
    import pytesseract
    from PIL import Image
    import io

    myconfig = r"--psm 6 --oem 3 -l " + language

    img = Image.open(io.BytesIO(await image.read()))

    text = pytesseract.image_to_string(img, config=myconfig)

    return text
