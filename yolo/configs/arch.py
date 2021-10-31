# Image dimensions, number of cells
INPUT_CONFIG = {
    "image_width": 448,
    "image_height": 448,
    "image_channels": 3,
    "S_grid": 7,
    "B_predictions": 2,
    "C_classes": 20
}


# (kernel_size, filters, stride, padding)
CNN_CONFIG = [
    "INPUT_LAYER",
    (7, 64, 2, 3),
    "MAX_POOL",
    (3, 192, 1, 1),
    "MAX_POOL",
    (1, 128, 1, 0),
    (3, 256, 1, 1),
    (1, 256, 1, 0),
    (3, 512, 1, 1),
    "MAX_POOL",
    [(1, 256, 1, 0), (3, 512, 1, 1), 4],
    (1, 512, 1, 0),
    (3, 1024, 1, 1),
    "MAX_POOL",
    [(1, 512, 1, 0), (3, 1024, 1, 1), 2],
    (3, 1024, 1, 1),
    (3, 1024, 2, 1),
    (3, 1024, 1, 1),
    (3, 1024, 1, 1),
]