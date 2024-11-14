'''
Author: Jack.Zhou
Date: 2024-11-14 16:25:31
LastEditTime: 2024-11-14 16:33:38
'''
'''
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的
盘子数量然后打印出把所有盘子从A借助B移动到C的方法，例如：
'''
# 汉诺塔Python视频讲解：https://www.bilibili.com/video/BV1Hk4y1k7KL/?spm_id_from=333.337.search-card.all.click&vd_source=12e71d00bf7e94411526774650e5cfad


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a, c, b)   #把A柱子上面的n-1个盘子，先全部放到B上面
        move(1, a, b, c)    #再把A柱子上剩下的一个盘子，放到C上面
        move(n-1,b, a, c)   #最后把B柱子上面的盘子借助A柱子，移动到C上面

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')