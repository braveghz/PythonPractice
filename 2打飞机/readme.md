# 打飞机

### pygame安装

```
brew install sdl smpeg sdl_image sdl_mixer sdl_ttf portmidi hg
pip install hg+http://bitbucket.org/pygame/pygame
```

Emmm you could try
```
sudo pip install pygame
```


### Tips

##### pygame

```python

pygame.init()	# initialize all imported pygame modules
pygame.quit()   # uninitialize all pygame modules
```

##### Rect

```
Rect(left, top, width, height) -> Rect # 存储坐标的pygame对象
Rect((left, top), (width, height)) -> Rect
Rect(object) -> Rect

rect的常用属性:
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
```

##### display

```python

pygame.display.set_mode()   # Initialize a window or screen for display
set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
# resolution代表(width,height)，flags代表其它选项集合，depth代表颜色位数(默认是 best and fastest color depth for system)
# flags的可选值【举例】
pygame.FULLSCREEN    create a fullscreen display


pygame.display.set_caption()    # Set the current window caption
set_caption(title, icontitle=None) -> None

pygame.display.flip()  # Update the full display Surface 全部更新
flip() -> None


pygame.display.update() # Update portions of the screen 可部分更新
update(rectangle=None) -> None # 不加参数则全部更新
update(rectangle_list) -> None

```


##### image

```
pygame.image.load()   # load new image from a file
load(filename) -> Surface
load(fileobj, namehint=””) -> Surface,namehint = original filename
```

##### Surface （代码中的screen）

```
blit()    # draw one image onto another
blit(source, dest, area=None, special_flags = 0) -> Rect
# dest表示距离左上角

subsurface()  # 子surface
subsurface(Rect) -> Surface

get_rect()  # get the rectangular area of the Surface
get_rect(**kwargs) -> Rect

```

##### key
```
pygame.key.get_pressed()   # the state of all keyboard buttons
get_pressed() -> bools     # ==1 则为按下了这个键
```

##### sprite

```
pygame.sprite.Group  # A container class to hold and manage multiple Sprite objects.
```