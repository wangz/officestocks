# -*- coding: utf-8 -*-
#author: wangzhuo
import  time

import  wx
import  wx.gizmos   as  gizmos
import urllib2,time,thread

work_state = False
def longRunning():
    global work_state
    while work_state:        
        p = urllib2.urlopen('http://hq.sinajs.cn/list=s_sh000001')
        sh = p.read()
        #win.SetTitle(sh.split('=')[1][1:-3].split(',')[1])
        wx.CallAfter(win.SetTitle,sh.split('=')[1][1:-3].split(',')[1])
        print sh.split('=')[1][1:-3].split(',')[1]
        time.sleep(2.5)

def do_go(evt):
    global work_state
    work_state = True
    thread.start_new_thread(longRunning, ())
    
def do_stop(evt):
    global work_state
    work_state = False
    win.SetTitle('oss')
    
def OnTimeToClose(evt):
    global work_state
    work_state = False
    win.Close()
    
app = wx.App()
win = wx.Frame(None,title=u"oss",size=(250,100))

menuBar = wx.MenuBar()
menu = wx.Menu()
menu.Append(wx.ID_EXIT, u"close")

win.Bind(wx.EVT_MENU, OnTimeToClose, id=wx.ID_EXIT)

menuBar.Append(menu, u"func")
win.SetMenuBar(menuBar)

bkg = wx.Panel(win)
btn_go = wx.Button(bkg,label=u"go",pos=(20,1))
btn_stop = wx.Button(bkg,label=u"stop",pos=(120,1))

btn_go.Bind(wx.EVT_BUTTON, do_go)
btn_stop.Bind(wx.EVT_BUTTON, do_stop)

win.Show() 
app.MainLoop() 

