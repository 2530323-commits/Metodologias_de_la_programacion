esptool --port COM8 erase-flash
esptool --port COM8 --baud 460800 write-flash 0x1000 ESP32_GENERIC-20250911-v1.26.1.bin
ampy --port COM8 put main.py