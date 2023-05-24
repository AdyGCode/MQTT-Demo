# MQTT Demo

## Activating the Local `venv`
This presumes you have a Python `venv` folder. It may 
be called `venv-306`, or similar.

- Open a command prompt
- Change into the folder with this project 
    - (use `cd` for this)
- On Windows run the command: `.\venv\Scripts\activate` 
    - (replace venv with the correct Python venv folder name)

This will activate the Python virtual environment (venv) ready 
for use.

NB: On ordinary command prompts, you are unlikely to 
see a `(venv)` at the start of the command line.

## Installing Packages

Run the following command in your `venv` based prompt:
```shell
python -m pip install paho-mqtt
```

Note: Shorthand for this is: `pip install paho-mqtt`.

## Subscriber
Filename: `subscriber.py`

### Pseudocode
- import mqtt client
- configure the client
- start the client
- listen forever
- when a message arrives - display it