import time

def focus_timer(minutes):
    """A function that runs a focus timer for a specified number of minutes."""

    # convert minutes to seconds
    seconds = minutes * 60

    # Loop through the countdown in seconds.
    for second in range(seconds, -1, -1):
      
        # calculate remaining minutes and seconds
        m, s = divmod(second, 60)
        
        # format the remaining time string
        time_display = '{:02d}:{:02d}'.format(m, s)
        
        # clear previous time display (using ANSI escape codes)
        print('\033[2K\033[1G', end='')
        
        # display the remaining time
        print('Remaining time: {}'.format(time_display), end='')
        
        # wait for 1 second
        time.sleep(1)

    print('\nTimer completed!\a')  # end the timer with a beep sound


# example usage
focus_timer(25)  # run a 25-minute focus session
