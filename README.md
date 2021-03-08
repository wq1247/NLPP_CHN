# NLPP_CHN
本文档包含New Love Plus+游戏字幕机翻汉化数据文件、文本源文件及开发文件。
由于本文档仅包含字幕文件，需配合NLPPGit使用!
因NLPPGit字库问题，以及大量文本未进行校对，导入本文档字幕文件后基本属于不可用状态。[IMG_0240](https://user-images.githubusercontent.com/80207563/110263053-7e227c80-7ff0-11eb-8fc5-b7c2c98b3022.jpeg)

1.根目录下程序文件为开发文件，均运行在 python3 环境下，全部为本人自主开发——
	xml2text.py 可以实现由.xml文件转.txt文件；
	Textpack2.py 可以实现目录下每35个.txt文件打包为1个.txt文件；
	Textpack.py 可以实现目录下所有.txt文件打包为1个.txt文件；
	unpack.py 可以实现由Textpack(2)打包的.txt文件还原为多个原.txt文件；
	mul_text2xml.py 为批量.txt文件转.xml文件工具；
	text2xml.py 为单一.txt文件转.xml工具；

2.Text文件夹内为纯文本文件.txt
	-内包含已经完成机翻的CHN文件夹及原始未翻译文件夹JPN、ENG
	
3.xml文件夹内已转换为.xml的字幕文件
	-内包含已经完成机翻的CHN文件夹及原始未翻译文件夹JPN、ENG

4.CHNdbin2文件夹内已打包为.dbin2游戏数据文件的字幕文件
	-已经完成机翻

受精力及能力所限，本人不在对本文档进行后续开发。

*本文档开发所使用的源文件来源于项目 https://github.com/Makein/NLPPGit

*.xml与.dbin2互相转换的工具为 https://github.com/gdkchan/NLPTextTool
