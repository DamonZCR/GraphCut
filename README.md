# GraphCut 图割

此项目以https://github.com/cm-jsw/GraphCut
项目为模板，这里的是自己环境下的一次运行和记录.
 
这次运行去除命令行交互方式，Run是傻瓜式的.

## 项目运行环境及要求
解释器：python3.7  
所需库函数(只需以下三个):

            1) numpy
            2) opencv-python
            3) PyMaxflow     
_注：PyMaxflow包可能不太容易安装，若安装失败，建议使用.whl文件下载安装.我使用的这个包放在resourse目录下备用，
下载 .whl包时，根据 **自己系统的版本** 对应着的 **包名** 下载;如：cp37代表python版本3.7;amd64代表Windows64位._


## 代码运行流程
1.在GraphCut.py文件点击运行  
2.使用鼠标进行前后背景标注,英文状态下，点击‘ t ’切换    
3.点击‘ g ’，进行切割  
4.详细功能：  
  （1）‘ esc ’：退出；  
  （2）‘ c ’：清除所有标注；  
  （3）‘ g ’：进行图片分割；  
  （4）‘ t ’：前后背景标准的切换；  
  （5）‘ s ’：将分割后的图片保存到输出文件  
