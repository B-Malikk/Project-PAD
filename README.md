# IT102C-5 PAD Project

## Introduction
This is the PAD project of IT102C-5 for the [Pepper robot](https://en.wikipedia.org/wiki/Pepper_(robot)).

Our project's goal was to develop an application for the Pepper robot to greet people coming into the HvA Wibauthuis
and to help them if needed.

## Setup
To run our application, one needs to run it in an environment with the following requirements:

- Python version 2.7.x - 32 bits
- NAOqi SDK installed (See [here](https://developer.softbankrobotics.com/nao6/naoqi-developer-guide/sdks/python-sdk/python-sdk-installation-guide) 
  for instructions and [here](https://www.softbankrobotics.com/emea/en/support/pepper-naoqi-2-9/downloads-softwares) for the download (Under "Old: Pepper SDK"))

Make sure to install the libraries listed in requirements.txt as well:
```
python -m pip install -r ./app/requirements.txt
```

## Running the application

To run the application, one needs to change the hostname and port in `main.py` to the hostname and port of their own Pepper robot.
Then, just run the following command:

```
python app/main.py
```

## Additional information

- The documentation for this project can be found under the `docs/` folder.
- A website has to be hosted somewhere, its HTML files can be found under `app/mirai/HTML/` and its url is loaded on the tablet in main.py
- The Main class is an MQTT subscriber as well, please do not run anything that blocks the main thread in it. (Such as `time.sleep()`)

## Contributors

- Evelien-Lillian Dekkers
- Bilal Malik
- Maverick van der Pol
- Ceren Kayapinar
- Bryan Visser
