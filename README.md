## Silo
An API for the missile launcher on Brian's desk

### Installation
1. Install PyUSB from [http://sourceforge.net/projects/pyusb/](http://sourceforge.net/projects/pyusb/)
2. `pip install -r requirements.txt`
3. `python run.py`
4. Browse to `http://<computer-IP-address-here>:5000/fire`. The launcher should fire a missile.

If you wish to run the application on Windows startup, place a shortcut to `runserver.bat` in the ~~victim's~~ user's Startup folder.

### Commands
`<amount>` below denotes the amount of time (measured in ms) for which to move the turret.
* `/left/?amount=<amount>` Move the turret left
* `/right/?amount=<amount>` Move the turret right
* `/up/?amount=<amount>` Move the turret up
* `/down/?amount=<amount>` Move the turret down
* `/fire/` Fire a missile
* `/reset/` Reset the launcher and turret to their starting positions