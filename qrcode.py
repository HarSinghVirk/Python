# Generating QR Code using Python
import qrcode as qr
img = qr.make("https://github.com/HarSinghVirk")
img.save("harvinder_github")