import threading
import cv2

class GCamera(threading.Thread):
    def __init__(self, **settings):
        super().__init__()
        self.gstreamer = self.gstreamer_pipeline(settings)
        self.daemon = True
        self.frame = None
        self.start()

    def gstreamer_pipeline(self, **settings):
        display_width = 1280
        display_height = 960
        return (
            "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                settings[0], # Capture Height
                settings[1], # Capture Width
                settings[2], # FPS
                settings[3], # Orientation
                display_width,
                display_height,
            )
        )


    # This isnt the best way of doing this due to OpenCV latency
    # Need to find a way to access camera stream
    def run(self):
        cap = cv2.VideoCapture(self.gstreamer, cv2.CAP_GSTREAMER)

        if cap.isOpened():
            while True:
                ret, self.frame = cap.read()
                key = cv2.waitKey(30)
                if key == ord('q'):
                    break
            cap.release()
                
        

    def get_frame(self):
        return self.frame
