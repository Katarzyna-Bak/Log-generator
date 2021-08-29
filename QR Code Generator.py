import qrcode

file = input('What do you want to make into QR Code? ')
img = qrcode.make(file)
name = input('How do you want to name the file? ') +'.jpg'
img.save(name)