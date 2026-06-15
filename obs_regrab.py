import os, time
import obsws_python as obs

pw = os.environ.get("OBS_WS_PASSWORD", "")
c = obs.ReqClient(host="localhost", port=4455, password=pw, timeout=5)

dev = "Hagibis:\\\\?\\usb#22vid_345f&pid_2130&mi_00#227&2bd8484c&0&0000#22{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global"

# Clear device id
c.set_input_settings("Switch", {"video_device_id": ""}, True)
print("cleared device id")
time.sleep(3)

# Restore device id
c.set_input_settings("Switch", {"video_device_id": dev}, True)
print("restored device id")
time.sleep(5)

# Re-activate just in case
try:
    c.press_input_properties_button("Switch", "activate")
    print("activate pressed")
except Exception as e:
    print("activate err:", e)
