import os
import sys
import platform

from PIL import Image, ImageDraw, ImageFont

RootDir = 'D:/old'
# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
if platform.system() == 'Windows':
    my_font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 24)
else:
    my_font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 24)


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
    # .text(text_xy, text, font=font, fill=(76, 234, 124, 180))
    image_draw.text(text_xy, text, font=font, fill=(254, 67, 101))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


# 遍历jpg文件
def find_jpg():
    jpg_list = []
    # rootdir = sys.path[0]
    list = os.listdir(RootDir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(RootDir, list[i])
        if os.path.isfile(path) and (path.endswith('.jpg') or path.endswith('.JPG')):
            print(path)
            jpg_list.append(path)
    return jpg_list


content = input('请输入需要添加的水印(例如：2017/11/24):')
jpg_path_list = find_jpg()
for jpg_path in jpg_path_list:
    im_before = Image.open(jpg_path)
    # im_before.show()
    im_after = add_text_to_image(im_before, content)
    # im_after.show()
    r, g, b, a = im_after.split()
    im_after = Image.merge('RGB', (r, g, b))
    if not os.path.exists(RootDir + '/new'):
        os.mkdir(RootDir + '/new')
    im_after.save(RootDir + '/new/' + os.path.basename(jpg_path))
input('转换完成，按回车结束进程')
