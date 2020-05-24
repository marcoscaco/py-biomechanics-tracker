def open_video_file(title):
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename(
        title=title,
        filetypes=[("Video files", ".mp4 .avi")]
    )
    return filename
