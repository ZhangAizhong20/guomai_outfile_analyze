### 问题
1. 文档中说运行过程会中断报错，为啥我没有
2.信息文件中各个列的来源和说明
3.td-idf 对应的算法聚类

### 2024.10.11思路整理
帮助编辑制定决策，确认编辑的确认文章的难点。
目前代码主要做的是给没有标签的书籍确认价值原型

如果想要大胆一点，帮助编辑分析整本书的内容
哪一本书，哪个题材，哪个价值原型，会有更好的表现
但分析表现还要排除一些其他因素，比如排除作者自带的流量，ip
就是figure out 这个项目的目的，我们做聚类，做分类的业务目标，如何进行盈利

竞品分析，是否都是作者主要的知识库

根据原始文稿自动胜场选题信息，价值原型等

研究当前投稿相关选题，找出难点，投稿的价值原型是否和公司的匹配，如果匹配，那不被接纳的原因又是什么
所以原因又被分为几类，和谁作为比较更合适，要求比较对象是通过审核的书籍，或者高消费的书籍，疑问，，

价值原型这个概念是谁提出来的，产品文档上有没有相关需求

希望思考对于目前上传的投稿文档，是否符合当前有关价值原型，如果符合怎样。

短期的预期，目前的外部选题是否符合果麦的价值原型，然后这些外部选题对应的价值原型的通过率是多少，如果不通过，否定的原因又是什么。

对于之前项目于形成的价值原型，对应的通过率样本又是什么，是不是已经是通过提案的选题，而实际上目前这些选题其实还没有通过提案

如果提取的价值原型符合果麦当前已有的价值原型，可以寻找和当前价值原型类似的文章进行分析？对比？有哪些不同？
还可以结合作者等相关信息

### 数据疑问：
选题和待分配选题是什么意思啊
为什么有的书籍通过了评审但是没有进入选题池进行审核呀

### 尝试大纲
已有外部选题相关数据

~ 图书名称，可能存在多个选题
~ 作者信息，姓名，是否出版过图书，作者简介
~ 赛道分类
~ 主题关键词
~ 简介或目录，简介的字数
~ 审核状态，初审直接不通过，被驳回，被二次初审等等
~ 原始文稿相关信息
~ 继续作者相关信息

# 千帆大模型prompt记录

现在拥有一个价值原型知识库，“价值原型”是一个能够简洁、直接地表达某种普遍价值或情感的模型或符号。它可以是国内外经典语录、中国古诗词、经典名句、俗语或者是一句高度凝练主题的有哲理的话，能够迅速被人们理解和接受，产生共鸣。

然后我现在有一个新书，我可以向你提供书的名称，类型，目录以及简介还有样张。我希望你能帮我判断这个新书是否符合知识库的一些价值原型。如果匹配那对应哪些价值原型我现在是一家出版公司，然后我

我需要你扮演出版公司的产品经理，出版公司往往会收到很多自由作者的投稿，其中就包括网文作者，我需要你判断接收到的投稿是不是网文

#### 模型初步尝试

    # 角色任务
作为图书内容总结专家，你的任务是基于用户提供的书籍信息，判断图书是否符合当前已有价值原型知识库。你需要首先判断内容是否高度匹配目前已拥有的价值原型。如果不匹配，你需要为这本书重新总结新的价值原型。

#### 工具能力

1. 书籍信息分析：你需要仔细分析用户提供的书籍名称、类型、目录、简介以及样张等信息，以理解书籍的核心价值和情感。
2. 应用设计：基于书籍信息分析，设计应用界面和功能，确保应用能够简洁、直接地展示书籍的价值原型。
3. 价值原型匹配：将书籍内容与价值原型知识库进行匹配，判断书籍文本内容是否与价值原型知识库相匹配，确定对应的具体价值原型，写出配对的价值原型百分比。

### 要求与限制

2. 快速传达价值理念：需要能够快速有效地传达书籍的价值理念，使用户产生共鸣。
3. 准确匹配价值原型：必须确保新书与价值原型知识库的匹配准确性，为用户输出和知识库中价值原型完全匹配的文本。
4. 应用输出格式：是否匹配知识库价值原型：来自知识库的价值原型1，来自知识库的价值原型2

## 模型的效果和进一步思考
根据目前模型的表现来看是超出预期的，奇迹般地不符合价值原型选题的竟然都被直接B掉了，但目前测试的样本数量相对较少，可以进一步展开进行统计测试。

模型出了一个新的问题，就是文本信息的问题，似乎是文本信息越多，越难以匹配的趋势
网文的问题，因为写的很多都是所谓的都市相关内容，这类文章中往往会提到女性主义等相关字眼，所以评判价值不大，难以匹配，很难有参考价值

我们或许还需要对文本进行进一步加工
### 对于过拟合问题，
根据之前的模型，果麦总结出来的价值原型排除了过拟合的问题，因为是现根据目前已有内容提取关键词再进行价值原型的提取。

根据价值原型，寻找图书，帮助编辑自行发掘选题

<p><span style="color:#f7c666;">内容简介</span></p><p>《三十六计》或称“三十六策”，是指中国古代三十六个兵法策略，语源于南北朝，成书于明清。它是根据我国古代卓越的军事思想和丰富的斗争经验总结而成的兵书，是中华民族悠久文化遗产之一。</p><p>&nbsp;</p><p>&nbsp;</p><p>目录</p><p>&nbsp;</p><p>第1 章　胜战计</p><p>第一计　瞒天过海</p><p>第二计　围魏救赵</p><p>第三计　借刀杀人</p><p>第四计　以逸待劳</p><p>第五计　趁火打劫</p><p>第六计　声东击西</p><p>第2 章　敌战计</p><p>第七计　无中生有</p><p>第八计　暗度陈仓</p><p>第九计　隔岸观火</p><p>第十计　笑里藏刀</p><p>第十一计　李代桃僵</p><p>第十二计　顺手牵羊</p><p>第3 章　攻战计</p><p>第十三计　打草惊蛇</p><p>第十四计　借尸还魂</p><p>第十五计　调虎离山</p><p>第十六计　欲擒故纵</p><p>第十七计　抛砖引玉</p><p>第十八计　擒贼擒王</p><p>第4 章　混战计</p><p>第十九计　釜底抽薪</p><p>第二十计　浑水摸鱼</p><p>第二十一计　金蝉脱壳</p><p>第二十二计　关门捉贼</p><p>第二十三计　远交近攻</p><p>第二十四计　假道伐虢</p><p>第5 章　并战计</p><p>第二十五计　偷梁换柱</p><p>第二十六计　指桑骂槐</p><p>第二十七计　假痴不癫</p><p>第二十八计　上屋抽梯</p><p>第二十九计　树上开花</p><p>第三十计　 &nbsp; 反客为主</p><p>第6 章　败战计</p><p>第三十一计　美人计</p><p>第三十二计　空城计</p><p>第三十三计　反间计</p><p>第三十四计　苦肉计</p><p>第三十五计　连环计</p><p>第三十六计　走为上计</p><p><span style="color:#f7c666;">阅读价值</span></p><p>《三十六计》是根据我国古代军事思想和丰富的斗争经验总结而成的智谋书，它精炼概括了中国谋略的全部精华，是中华民族智慧宝库中的经典，与著名的《孙子兵法》并称为世界军事史上的双璧。</p><p><strong>本书典故较多，又涉及到众多历史 例案 ，比较适合改编成漫画。</strong></p><p>&nbsp;</p><p>&nbsp;</p>

