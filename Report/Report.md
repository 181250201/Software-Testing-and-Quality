# AutomatedTesting2020

姓名：郑阳

学号：181250201

选题方向：移动测试大作业

***



### 代码框架与思路

#### 数据解析

犹豫json文件的不完整性，我们需要对数据进行处理。有些bounds和rel-bounds并不一致，有的bounds对应的控件对于控件类型的标志并不准确，是一个所有控件类型的父类，不一致的bounds需要我们判断准确性。有的控件数据存在冗余的标注，也需要我们进行处理。

对json文件进行遍历，使用深度优先或者广度优先的搜索方式对数据集进行搜索，作业中使用的是深度优先算法对json遍历，删除不符合要求的控件，得到控件类型和坐标，生成json文件

### 运行步骤

firststep.py是第一部分的代码入口

### 相关参考文献

潘金赤.GUI自动化测试平台的技术以及应用研究.华中科技大学，2010

许志兴，唐晓纹，刘学军.移动终端软件自动化测试技术的研究与应用.南京工业大学学报（自然科学版），2006（5）

陆永忠，汪春，聂松林.GUI自动化测试用例生成策略的研究.系统工程与电子技术

张倩倩，基于控件识别的GUI自动化测试工具的研究与实现，2015-东南大学：软件工程

自动化测试中基于GUI非标准控件的识别和应用

http://uied.online/

https://pytorch.org/docs/stable/torchvision/models.html#faster-r-cnn

https://github.com/eriklindernoren/PyTorch-YOLOv3

https://github.com/Duankaiwen/CenterNet



## 结果示例

![1605959756633](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\1605959756633.png)

![1605959833009](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\1605959833009.png)

## 个人感想

当时看到这个题目的时候觉得很有意思就选了这个方向，等到开始做的时候发现好难，网上也没有查到一些有针对性的资料，数据集的原作者没有标注数据的含义，光是看懂数据集就花了很长时间，刚开始和同学讨论了很久也没有什么进展，理解题目意思很困难，主要是没有什么思路，最后也只做了第一部分数据解析，对训练数据进行了一些预处理，得到了data.json

对于第二阶段的控件识别，我没有实现，在这里写一点对方法的理解。