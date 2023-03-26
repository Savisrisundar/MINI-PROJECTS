import qrcode
data='Don\'t forget to subscribe'
image=qrcode.make(data)
image.save('C:/Users/savis/Documents/PYTHON/myqrcode.png')
