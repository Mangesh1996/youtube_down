import wx


app=wx.App()
window=wx.Frame(None,title="Youtube Downloader",size=(500,400))
panel=wx.Panel(window)
label=wx.StaticText(panel,label="test",pos=(100,50))
img=wx.Image("/home/diycam/Desktop/work/youtub_downloader/youtub_downloader.png",wx.BITMAP_TYPE_ANY)
imageBitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.BitmapFromImage(img))
window.Show()
app.MainLoop()

