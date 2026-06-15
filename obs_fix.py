import os, sys, time
import obsws_python as obs

pw = os.environ.get("OBS_WS_PASSWORD", "")
c = obs.ReqClient(host="localhost", port=4455, password=pw, timeout=5)

r = c.get_input_list()
names = [i["inputName"] for i in r.inputs]
print("inputs:", names)

target = "Switch"
if target in names:
    kind = [i["inputKind"] for i in r.inputs if i["inputName"] == target][0]
    print("kind:", kind)
    # Toggle device activation (dshow_input has an 'activate' button property)
    try:
        c.press_input_properties_button(target, "activate")
        print("pressed activate (1st: deactivate)")
        time.sleep(2)
        c.press_input_properties_button(target, "activate")
        print("pressed activate (2nd: reactivate)")
    except Exception as e:
        print("button press failed:", e)
        # fallback: toggle settings
        s = c.get_input_settings(target)
        print("settings:", s.input_settings)
