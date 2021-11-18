class HardwareInterface:

    '''
    A simple controller 'outline' for the NVIDIA jetson
    '''

    # Power and Hardware Options

    '''
    set_idle_hours
    No object detection is performed in this period. 

    :param t1: start time for idle (datetime)
    :param t2: end time for idle (datetime)
    :returns: Jetson status
    '''

    def set_idle_hours(t1, t2):
        pass


    '''
    set_idle_period
    Specify an amount of time for the device to be idle.

    :param period: (datetime) amount of time to idle for
    :returns: Jetson status
    '''

    def set_idle_period(period):
        pass


    '''
    perform_hardware_reset()
    Reboot the Jetson

    :returns: Jetson status
    '''

    def perform_hardware_reset():
        pass



    '''
    get_hardware_statistics()
    Return detailed statistics
    - Temps (all)
    - Component usage statistics

    :returns: JSON object with statistics 
    '''

    def get_hardware_statistics():
        pass


    # Set image frequency

    '''
    set_frame_rate()
    Set frame rate at which jetson performs object detection

    :param fps: Frames Per Second (FPS)
    :returns: Status
    '''

    def set_frame_rate(fps):
        pass


    # Receive Data

    '''
    get_data_csv()
    Get data csv
    Resets data pass csv to avoid duplicates

    :returns: Status
    '''

    def get_data_csv():
        pass


    '''
    get_single_result()
    Performs a singular object detection
    Interrupts main execution for one iteration for one image.

    :param img: input image (bits)
    :returns: count (bytes)
    '''


    def get_single_result(img):
        pass



    