from pytube import YouTube
YouTube(input("Enter YouTube URL: ")).streams.filter(mime_type='audio/mp4',only_audio=True).first().download('download')
print("Done")
