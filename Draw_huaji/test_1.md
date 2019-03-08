# <center>**说明文档**</center>
## 1. 设计目标
&emsp;&emsp;用python的turtle库绘制“滑稽表情”。

&emsp;&emsp;要求如下：

- 代码包含函数定义、分支和循环语句；
- 不低于50行；
- 代码中包含充分的注释和说明；
- 提供说明文档；
- 上传到Github；

## 2. 编程思路
&emsp;&emsp;先在网上找一张滑稽表情图片，随后对图片进行分析，确定绘制过程。因此在画图之前需要将图片分隔成基本图形（方块，圆弧，特殊曲线等），这样创作起来就相对容易了。

<img src="https://img-blog.csdnimg.cn/20190303003629469.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0hvbGx5UmFu,size_16,color_FFFFFF,t_70" width = "200" height = "200" div align=center />

&emsp;&emsp;通过分析发现，该图片主要由基本的圆组成，脸、眼睛、嘴巴以及眉毛不是圆就  
是圆弧，最多填充颜色，所以实现起来较为简单。  
&emsp;&emsp;在turtle中，不管是pencolor还是fillcolor都需要颜色（实际上并不推荐直接使用  RGB颜色，即颜色的英文名），推荐使用 [**颜色代码**](https://www.114la.com/other/rgb.htm"颜色代码对照表")。  
&emsp;&emsp;将滑稽图片分成脸、嘴巴、眉毛还有眼睛四部分，其中瞳孔包含在眼睛里。  
&emsp;&emsp;实现方法也很简单，先建立一张画布，然后依次画出目标表情的各个部分，最后统筹到一起即可。  
&emsp;&emsp;下面是各个函数功能的讲解。
### (1) __init__()
&emsp;&emsp;图片大小设置，考虑到表情为原型，故控制参数为radius（半径）。
### (2) drawingset()
&emsp;&emsp;顾名思义，画布的设置，本例中，画布设置为800x600像素大小。
### (3) my_goto()
&emsp;&emsp;画笔绘制的起落点控制函数。
### (4) face()
&emsp;&emsp;脸部，形状是一个圆，颜色是黄色。
### (5) mouth()
&emsp;&emsp;嘴巴，半圆弧，颜色是深棕色。
### (6) eyebrow(kind)
&emsp;&emsp;眉毛。注意这里眉毛分为左眉毛和右眉毛，kind参数的作用就是用来选择。这里使用了if条件语句：  
```python
if kind == 'left':
            self.my_goto(-60, 70)
            tt.left(45)  # 左转45°
            tt.circle(self.radius - 100, 60)
        elif kind == 'right':
            self.my_goto(100, 90)  
            tt.left(-30)  # 左转-30°
            tt.circle(self.radius - 100, 60)
```
### (7) eyes()
&emsp;&emsp;眼睛及部分，这里眼眶近似为双曲线，眼睛则为原型。分别填充白色和黑色。

## 3. 运行结果
<img src="https://img-blog.csdnimg.cn/20190309002540104.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0hvbGx5UmFu,size_16,color_FFFFFF,t_70" width = "200" height = "200" div align=center />  
&emsp;&emsp;差距稍微有点大吼~但是好歹神似，再改进吧。  
&emsp;&emsp;**代码及说明文档已上传到Github:** <https://github.com/Jadenmiao/Elective-Courses>  
## 4. 参考资料  
(1) 教学课件    
(2) 用turtle绘制哆啦A梦：  
&emsp;&emsp;https://github.com/PerpetualSmile/Python-Painting-Doraemon



