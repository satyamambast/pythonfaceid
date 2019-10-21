import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class App:
    def __init__(self, window_title, video_source=2):
        self.window = tkinter.Tk()
        self.window.title(window_title)
        self.video_source = video_source
        self.window.geometry("1000x1000")
        self.vid = videoCapture(self.video_source)

        self.canvas = tkinter.Canvas(self.window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        self.btn_snapshot=tkinter.Button(self.window, text="Enroll", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True) 
        self.delay = 15
        self.update() 
        self.window.mainloop()
    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
class videoCapture:
    def __init__(self, video_source=0):
         self.vid = cv2.VideoCapture(video_source)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
         if self.vid.isOpened():
             ret, frame = self.vid.read()
             if ret:
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
         else:
             return (ret, None)
    def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
 

App("Tkinter and OpenCV")