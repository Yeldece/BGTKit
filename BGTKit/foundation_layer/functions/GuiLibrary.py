import wx
app=wx.App()
frame=wx.Frame(None,title="default")
panel=wx.Panel(frame)
def CreateWindow(title):
    frame.SetTitle(title)
    frame.Show()
    app.MainLoop()
def InputBox(title,text):
    input=wx.TextEntryDialog(None,text,title)
    if input.ShowModal()==wx.ID_OK:
        result=input.GetValue()
        input.Destroy()
        return result
def MessageBox(title,text):
    wx.MessageBox(text,title)
def CreateButton(name,function):
    button=wx.Button(panel,label=name)
    button.Bind(wx.EVT_BUTTON,function)
def CreateTextbox(function,title=""):
  txt=wx.TextCtrl(panel,-1,style=wx.TE_PROCESS_ENTER,value=title)
  txt.Bind(wx.EVT_TEXT_ENTER,function)
