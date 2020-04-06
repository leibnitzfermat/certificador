from PIL import Image, ImageDraw, ImageFont

convidados = [
    "Leibnitz",
    "james",
    "karoline",
    "Lola"
]

font1 = ImageFont.truetype("./fonte1.ttf", size=45)

font3 = ImageFont.truetype("./fonte3.ttf", size=30)

for convidado in convidados:

    image = Image.open("123.jpg").convert("RGBA")

    lapis = ImageDraw.Draw(image)

    lapis.text(
        (250, 130),
        text="CERTIFICADO",
        fill="#0000",
        align="center",
        font=font1
    )

    lapis.line(
        (80, 173, 620, 173),
        fill="#0000",
        width=5,
    )

    lapis.text(
        (80, 330),
        text=f"Certificamos que o(a) {convidado} \nparticipou da I fórum de contabilidade ",
        fill="#0000",
        align="center",
        font=font3
    )

    lapis.line(
        (80, 930, 620, 930),
        fill="#0000",
        width=5,
    )

    image.save(f"certificado_{convidado}.png")
