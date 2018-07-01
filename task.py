import pyqrcode
qr_code = pyqrcode.create('https://github.com/eslutskaya/6semestr')
qr_code.svg('qr_code.svg', scale=7, module_color='maroon',  background='yellow')
qr_code.eps('qr_code.eps', scale=3)
print(qr_code.terminal(quiet_zone=1))
