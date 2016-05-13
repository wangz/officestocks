# -*- coding: utf-8 -*-
#author: wangzhuo
import  time

import  wx
import  wx.gizmos   as  gizmos
import urllib2,time,thread

import logging  
logging.basicConfig(filename='oss.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  

##logging.info('So should this')  
##logging.warning('And this, too')

SZZ='http://hq.sinajs.cn/list=s_sh000001'

CYB='http://hq.sinajs.cn/list=s_sz399006'

DATASOURCE={}
DATASOURCE['zbcm']='http://hq.sinajs.cn/list=sh600633'
DATASOURCE['yywl']='http://hq.sinajs.cn/list=sh600588'
DATASOURCE['zzny']='http://hq.sinajs.cn/list=sz000816'

count = 0
work_state = False
def longRunning():
    global work_state,count
    while work_state:
        try:
            datas = DATASOURCE.items()
            for item in datas:
                p = urllib2.urlopen(item[1])
                sh = p.read()
                #win.SetTitle(sh.split('=')[1][1:-3].split(',')[1])
                res = sh.split('=')[1][1:-3].split(',')
                buy1 = float(res[11])
                sail1 = float(res[21])
                xx = sail1 - buy1
                if xx > 0.021:                
                    wx.CallAfter(win.SetTitle,item[0]+str(xx))
                    logging.info('buy %s--------%s------%s' % (sh,' ','buy:'+str(xx)))
                logging.info('%s,%s,%s' % (count,item[0],sh.split('=')[1][1:-3].split(',')[1]))
        except Exception,e:
            logging.warning(str(e))   
        count+=1 
        time.sleep(1.5)

def do_go(evt):
    global work_state
    work_state = True
    thread.start_new_thread(longRunning, ())
    
def do_stop(evt):
    global work_state
    work_state = False
    win.SetTitle('remind')
    
def OnTimeToClose(evt):
    global work_state
    work_state = False
    win.Close()
    
app = wx.App()
win = wx.Frame(None,title=u"remind",size=(250,100))

menuBar = wx.MenuBar()
menu = wx.Menu()
menu.Append(101, u"setting")
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

