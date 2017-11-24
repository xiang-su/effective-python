from PIL import Image, ImageDraw, ImageFont

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
my_font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 24)


# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=my_font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = (rgba_image.size[0] - text_size_x - 10,
               rgba_image.size[1] - text_size_y - 10)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


im_before = Image.open("1.png")
im_before.show()
im_after = add_text_to_image(im_before, '2017/11/24')
im_after.show()
im_after.save('im_after.jpg')
