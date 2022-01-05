import ctypes
import numpy as np
import cv2
import tensorrt as rt
import pycuda.drive as cd
from tensorRT import common

MODEL = 'yolo/yv4-crowdhuman.trt'

try:
    ctypes.cdll.LoadLibrary('./plugins/libyolo_layer.so')
except OSError as exception:
    raise SystemExit('YOLOv4 is not built.')

class TensorRTYV4():
    def __init__(self):

        # Model directory
        self.model_trt_file = MODEL

        # Load TensorRT engine
        try:
            with open(self.model_trt_file, 'rb') as model, rt.Runtime(rt.Logger.INFO) as runtime:
                self.engine = runtime.deserialize_cuda_engine(model.read())
        except FileNotFoundError:
            raise SystemExit('Model does not exist.')
        
        # Allocate CUDA buffers
        self.inputs, self.outputs, self.bindings, self.stream = common.allocate_buffers(self.engine)

        # Create execution context
        self.context = self.engine.create_execution_context()
    
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
                608, # Capture Height
                608, # Capture Width
                10, # FPS
                0, # Orientation
                display_width,
                display_height,
            )
        )

    def _detect_gstreamer_yolo(self, frame):
        
        # Load frame from Gstreamer to GPU
        self.inputs[0].host = np.ascontiguousarray(frame)

        # 
        yolo_7_tensors_op = common.do_inference_v2(
            context  = self.context, 
            bindings = self.bindings, 
            inputsvv = self.inputs, 
            outputs  = self.outputs, 
            stream   = self.stream)
        
        # [x,y,w,h,conf,class,prof]
        for output_tensor in yolo_7_tensors_op:
            print(output_tensor)


        