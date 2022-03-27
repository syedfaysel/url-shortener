from pytube import YouTube

link = input("Enter link:")
print("Downloading")
YouTube(link).streams.first().download()
print("Downloaded Successfully")
