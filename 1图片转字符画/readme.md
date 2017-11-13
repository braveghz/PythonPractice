# 图片转字符画

### solution

RGB算灰度

```
gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
```

根据图片算出来的灰度  白色255 / 黑色 0

写一个无重复的字符集list

`list[0....length]` 对应 灰度 `小...大`

gray/256.0 * length


大概就是这个意思 2333 找简体画还行，复杂的小姐姐图片就效果很差了


### tips整理

#### argparse

命令行解析

```
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--height', type=int, help='height of image', default=50) # 添加参数
args = parser.parse_args() # 得到参数
```

比如说
```
python main.py -i banana.jpg --width 80 --height 80 -o output.txt
```

默认参数类型 字符串， -- 表示可选参数，这样

```
args.i = banana.jpg
args.width = 80
```


#### Image

###### 安装 Pillow
```
# MAC
brew install libtiff libjpeg libpng webp little-cms2 freetype
sudo pip install Pillow
```

###### Image

```
from PIL import Image
image = Image.open(sourceFile)
```

实例有5个属性
- format: 格式（JPG, PNG, BMP, None, etc.
- mode: 模式（RGB, CMYK, etc.
- size: tuple (width, height)
- palette: 仅当 mode 为 P 时有效，返回 ImagePalette
- info: 实例信息

###### resize函数

```
im.resize(size) ⇒ image
im.resize(size, filter) ⇒ image
```

size 参数应该是`(width, height)`这种，filter默认为`NEAREST` (use nearest neighbour)

###### getpixel函数

```
im.getpixel(xy) ⇒ value or tuple
```

返回给定位置的像素，如果图片是`multi-layer`则返回`tuple(r,g,b)`


