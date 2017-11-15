# 3兔子

类似于打飞机小游戏

### pygame

##### mouse

```
pygame.mouse.get_pos()  #  cursor position
get_pos() -> (x, y)
```

##### transform
```
pygame.transform.rotate()  # rotate an image 旋转
rotate(Surface, angle) -> Surface

```

### Bug

1. up/down/right/left重复多次，兔子移动变重影

    全部界面running刷新一遍，因为以前画的内容并没有消失
   ，只是重新画一个新的位置的兔子+原本的其他东西


2. 兔子旋转

    1. surface的get_pos为左上角坐标
    2.

        ```
        player1 = pygame.transform.rotate(player, angle)
        player = pygame.transform.rotate(player, angle) # 这样写 兔子会快速跑走？
        ```