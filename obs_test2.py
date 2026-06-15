import os, time
import obsws_python as obs

pw = os.environ.get("OBS_WS_PASSWORD", "")
c = obs.ReqClient(host="localhost", port=4455, password=pw, timeout=5)

# Screenshot the Switch source twice, 2s apart, to fresh files
for n in (1, 2):
    c.send("SaveSourceScreenshot", {
        "sourceName": "Switch",
        "imageFormat": "png",
        "imageFilePath": rf"C:\Users\ushid\Documents\FablePlaysPokemon\probe_{n}.png",
    }, raw=True)
    time.sleep(2)

# Also get source active state
st = c.send("GetSourceActive", {"sourceName": "Switch"}, raw=True)
print("source active:", st)

# Check media/device specific: get input settings
s = c.get_input_settings("Switch")
print("settings:", s.input_settings)
