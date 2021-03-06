# find_corpus



你是否只知道一个短语而不知道如何写成句子？你是否只记得单词中的几个字母却想不出来整个单词？

英文写作语料搜索🔍神器。强大的模糊查询功能，帮助你的英文学术写作更地道。

## 示例

<img alt="demo1" src="http://www.xyu.ink/wp-content/uploads/2020/11/corpus2.png" width=800>

## 环境需求

全平台 Windows/Linux/Mac 

Python >= 3.6

## 准备txt格式的语料素材

准备你自己的语料素材，它们可以来源于文章、杂志、维基百科等等，并把它们都制作成txt格式。

搜集这些材料需要简单的网络爬虫知识，如果你不知道如何制作自己的语料库，我们提供了一份CVPR2018-2020的语料材料以供参考。 [[下载链接](http://www.xyu.ink/wp-content/uploads/2020/11/CVPR_18-20.zip)].

## 运行这个程序

1. 在`find_corpus.py`中将`root_dir`设置成你自己的语料文件夹(下载解压后的文件夹路径).

2. 运行下面的命令

   ```bash
   python find_corpus.py
   ```

3. 输入要查询的单词或者短语，单独的问号( ? )表示匹配任何**一个**单词，星号( \* )表示匹配**一或多个**单词，括号中加中竖线(|)表示从几个单词中选择，与单词紧接的问号表示只记得单词的一部分，如(congra?tion)，在最前面加上三个井号(###)可以显示上下文：

   ```bash
   pattern:
     >>> as ? in fig             ? 匹配任意一个单词
     >>> code * publicly         * 匹配 1~n 个单词
     >>> (show|provide) results  (A|B|C) 匹配多个单词中的一个
     >>> show[ns]? ? results     正则表达式匹配
     >>> comparison is ?ed       匹配以ed结尾的单词
     >>> ### ? feature fusion    在开头加上 ### 可以显示上下文的语境
     >>> show all                显示上一次搜索所有的结果
     >>> exit                    退出
   ```

4.  等待查询的结果，因为搜索若干txt文件需要一些时间。


