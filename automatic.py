# imports
import os
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver
from utils.yolo_with_plugins import TrtYOLO
from jetson_utils.gcam import GCamera


# params
model = ''
confidence_threshold = 0.5

class Automatic(object):
    def __init__(self):
        self.gcam = GCamera(cap_height = 608, cap_width = 608, fps = 29, orientation = 2)
        self.count = 0
 
    # Need to integrate Gcamera once stream properly initialised
    def detection(self):
        cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
        if cap.isOpened():
            while True:

                # Get frame
                ret, frame = cap.read()

                # Get metrics from yolov4cococrowd
                bb, confidence, classes = trt_yolo.detect(frame, confidence_threshold)
                
                # Print bounding boxes
                ## bb in array format
                for b in bb:
                    # Box coords
                    [x_min, y_min, x_max, y_max] = b
                    cv2.rectangle(
                        frame, 
                        (x_min, y_min), 
                        (x_max, y_max), 
                        (0,0,255), 
                        2
                    )

                # Print number of people
                cv2.putText(
                    frame, 
                    self.det_num_bb(bb), 
                    (10,450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    3,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )

                # Need to implement a count to get x amount of frames to calculate average
                self.count += 1

                
                
                # Output to frame
                cv2.imshow("Automatic People Counting Camera", frame)
                key = cv2.waitKey(30)
                if key == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()


    def det_num_bb(self, bb):
        # method allows for some noise reduction implementation
        return len(bb)

    def calculate_average(self, counts):
        # very basic average across a number of frames, probs a method to do this with a list lol
        sm = 0
        for cnt in counts:
            sm += cnt
        return sm / len(counts)

    def to_api(self, count):
        pass

def run():
    auto = Automatic()
    auto.detection()

if __name__ == '__main__':
    run()