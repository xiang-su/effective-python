import os
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
    if image.size[0] > 1000:
        image = image.resize((1000, int(image.size[1] / (image.size[0] / 1000))), resample=1)

    if image.size[1] > 1000:
        image = image.resize((int(image.size[0] / (image.size[1] / 1000)), 1000), resample=1)

    image_draw = ImageDraw.Draw(image)
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(image)
    text_xy = (image.size[0] - text_size_x - image.size[0] * 0.07,
               image.size[1] - text_size_y - image.size[1] * 0.07)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(255, 108, 27))
    return image


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
    im_after = add_text_to_image(im_before, content)
    if not os.path.exists(RootDir + '/new'):
        os.mkdir(RootDir + '/new')
    im_after.save(RootDir + '/new/' + os.path.basename(jpg_path))
input('转换完成，按回车结束进程')
