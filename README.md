# officestocks
for check stocks in office 办公室看股软件

直接使用release-windows里解压后打开oss.exe即可

## logs
20241028 修复了新浪接口请求拒绝的问题

## 开发环境
使用python2.7环境

1.安装python。可以下载ANACONDA来安装，比较方便，创建PYTHON 2.7环境。

2.安装wxpython

3.双击oss.pyw即可，点击go,最小化后标题显示数字为股票指数

效果图：https://github.com/wangz/officestocks/wiki

## 开发
打包EXE
pyinstaller -w --icon=ico\Money_bag_dollar_128px_1198356_easyicon.net.ico oss.pyw

## mac 上使用方式
切到我建的虚拟环境：使用python2.7
>conda activate myevnname

安装python.app

>conda install -c conda-forge python.app

之后用pythonw运行
>pythonw main.py





