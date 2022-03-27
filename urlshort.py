import pyshorteners
link = input("Enter your link to shorten  : ")

s = pyshorteners.Shortener()
print(s.tinyurl.short(link))
