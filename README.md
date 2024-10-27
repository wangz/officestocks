# officestocks
for check stocks in office 办公室看股软件

直接使用release-windows里解压后打开oss.exe即可

#开发环境

#安装

1.安装python

2.安装wxpython

可以去官网下载，找不到的话可从这里下载：http://pan.baidu.com/s/1qXbznWS

3.双击oss.pyw即可，点击go,最小化后标题显示数字为股票指数

效果图：https://github.com/wangz/officestocks/wiki


#开发
打包EXE
pyinstaller -w --icon=ico\Money_bag_dollar_128px_1198356_easyicon.net.ico oss.pyw

#mac 上使用方式
切到我建的虚拟环境：使用python2.7
>conda activate myevnname
安装python.app
>conda install -c conda-forge python.app
之后用pythonw运行
>pythonw main.py




#log
20241028 修复了新浪接口请求拒绝的问题