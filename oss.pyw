# -*- coding: utf-8 -*-
#author: wangzhuo
import  time

import  wx
import  wx.gizmos   as  gizmos
import urllib2,time,thread

def longRunning():        
        while True:        
            p = urllib2.urlopen('http://hq.sinajs.cn/list=s_sh000001')
            sh = p.read()
            #win.SetTitle(sh.split('=')[1][1:-3].split(',')[1])
            wx.CallAfter(win.SetTitle,sh.split('=')[1][1:-3].split(',')[1])
            print sh.split('=')[1][1:-3].split(',')[1]
            time.sleep(2.5)

def doshutdown(evt):
    thread.start_new_thread(longRunning, ())

app = wx.App()
win = wx.Frame(None,title=u"help",size=(250,200))

bkg = wx.Panel(win)
btn = wx.Button(bkg,label=u"go",pos=(1,1))
btn.Bind(wx.EVT_BUTTON, doshutdown)


win.Show() 
app.MainLoop() 

