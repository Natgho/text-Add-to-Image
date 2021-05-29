# Created by Sezer Bozkir<admin@sezerbozkir.com>
from PIL import Image, ImageFont, ImageDraw


def add_angle_text(text: str,
                   img: Image,
                   angle: int = 0,
                   text_size: str = 26,
                   color: str = "#000",
                   font_type: str = 'Arial Bold.ttf',
                   position: tuple = (1055, 170)):
    # template_img = Image.open(img).convert("RGBA")
    original_image_size = img.size

    font = ImageFont.truetype(font_type, text_size)
    # calculate text size in pixels (width, height)
    text_size = font.getsize(text)
    # create image for text
    text_image = Image.new('RGBA', text_size, (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    # draw text on image
    text_draw.text((0, 0), text, font=font, fill=color)
    # rotate text image and fill with transparent color
    rotated_text_image = text_image.rotate(angle, expand=True, fillcolor=(0, 0, 0, 0))

    watermarks_image = Image.new('RGBA', original_image_size, (255, 255, 255, 0))
    watermarks_image.paste(rotated_text_image, position)

    combined_image = Image.alpha_composite(img, watermarks_image)
    # combined_image.save("output.png")
    return combined_image


def add_multiline_text(text: str, img, position: tuple, split_loop_size: int = None):
    if split_loop_size and len(text) > split_loop_size:
        for append_new_line in range(split_loop_size, len(text), split_loop_size):
            text = text[:append_new_line] + "\n" + text[append_new_line:]
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial Bold.ttf", size=24)
    draw.text(position, text, font=font, fill="#000")
    return img
