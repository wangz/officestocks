# -*- coding: utf-8 -*-
#author: wangzhuo
import  time

import  wx
import  wx.gizmos   as  gizmos
import urllib2,time,thread
from wx.lib.wordwrap import wordwrap

import logging,sys

reload(sys)                      
sys.setdefaultencoding('utf-8')

logging.basicConfig(filename='oss.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  

##logging.info('So should this')  
##logging.warning('And this, too') 

count = 0
work_state = False
headers = {'referer': 'http://finance.sina.com.cn'}
def longRunning(val):
    global work_state,count
    url = "http://hq.sinajs.cn/list=s_%s%s"
    loc = ""
    if len(val) !=8 :
        if val[0:3] in ("600","601","602"):
            loc = "sh"
        elif val[0:3] in ("300","002","000","399"):
            loc = "sz"
        else:
            loc = "sh"
    while work_state:
        try:
            req = urllib2 . Request (url % (loc,val),headers=headers)
            p = urllib2.urlopen(req)
            sh = p.read()
            #win.SetTitle(sh.split('=')[1][1:-3].split(',')[1])
            wx.CallAfter(win.SetTitle,sh.split('=')[1][1:-3].split(',')[1])
            logging.info('%s,%s,%s' % (count,' ',sh.split('=')[1][1:-3].split(',')[1]))
        except Exception,e:
            logging.warning(str(e))   
        count+=1 
        time.sleep(2.5)

def do_go(evt):
    global work_state
    val = tx1.GetValue()
    if len(val) in (6,8):
        work_state = True
        thread.start_new_thread(longRunning, (val,))
    
def do_stop(evt):
    global work_state
    work_state = False
    win.SetTitle('oss')
    
def OnTimeToClose(evt):
    global work_state
    work_state = False
    win.Close()

def about(evt):
    info = wx.AboutDialogInfo()
    info.Name = "Office Stocks"
    info.Version = "1.0"
    info.Copyright = "2017 Programmers and Coders Everywhere"
    info.Description = wordwrap(
        "A \"Office Stocks\" program is a software program that help people "
        "check stocks in office. ",
        350, wx.ClientDC(win))
    info.WebSite = ("https://github.com/wangz/officestocks/wiki", "Office Stocks")
    info.Developers = [ "wangzhuo1987@gmail.com", ]

    #info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

    wx.AboutBox(info)

    
app = wx.App()
win = wx.Frame(None,title=u"oss",size=(250,130))

menuBar = wx.MenuBar()
menu = wx.Menu()
menu.Append(101, u"setting")
menu.Append(102, u"about")
menu.Append(wx.ID_EXIT, u"close")


win.Bind(wx.EVT_MENU, OnTimeToClose, id=wx.ID_EXIT)
win.Bind(wx.EVT_MENU, about, id=102)


menuBar.Append(menu, u"func")
win.SetMenuBar(menuBar)

bkg = wx.Panel(win)
btn_go = wx.Button(bkg,label=u"go",pos=(20,30))
btn_stop = wx.Button(bkg,label=u"stop",pos=(120,30))

btn_go.Bind(wx.EVT_BUTTON, do_go)
btn_stop.Bind(wx.EVT_BUTTON, do_stop)

wx.StaticText(bkg, -1, 'focus:',pos=(45,2))
tx1 = wx.TextCtrl(bkg,-1,"sh000001", size=(80, 20),pos=(120,2))

win.Show() 
app.MainLoop() 

