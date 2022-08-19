# Arduino port name
# should be COM3, COM4 etc on windows and dev/tty... in linux
port = "COM5"
# File start indicator bytes
file_ind_bytes = "\x05"
# Waiting time (in second) for serial-read function
wait = 0.2
# Delay after sending file start signal(in ms)
file_start_delay = 1.2