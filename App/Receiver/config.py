# Arduino port name
# should be COM3, COM4 etc on windows and dev/tty... in linux
port = "/dev/ttyACM0"
# File indicator bytes set in arduino
file_ind_bytes = "\x05"
# Message indicator bytes set in arduino
msg_ind_bytes = "\x06"
# Waiting time (in second) for serial read function
wait = 0.2