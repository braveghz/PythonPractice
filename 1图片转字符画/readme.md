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


### 用到的tips整理

argparse

PIL

image.resize((width, height))

image2char(image.getpixel((j, i)))


