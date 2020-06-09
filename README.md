### A polybar plugin to measure average typing speed

![info-hackspeed](screenshots/1.png)

`refresh_minutes` decares after how many minutes the average resets.

Credit to: https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/info-hackspeed

#### Setup

Change `KEYBOARD_ID` to your specific device. List all devices using `xinput list`.

Adapt to your location of the script.

```python
proc = subprocess.Popen(
	"~/.config/polybar/scripts/info-avg-hackspeed/info-hackspeed.sh", shell=True, stdout=subprocess.PIPE
)
```

#### Module

```ini
[module/info-avg-hackspeed]
type = custom/script
exec = LOCATION
tail = true
```