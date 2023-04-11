# GVE DevNet ACI Port Usage

This prototype utilizes the ACI REST API to provide an overview of the node's interfaces within the fabric. The Python Flask application shows the total number of interfaces, the number of used of interfaces, the number of free interfaces (operational status down) and the number of reserved interfaces (description of Reserved). 

![/IMAGES/overview.png](/IMAGES/overview.png)

## Contacts
* Roaa Alkhalaf

## Solution Components
* ACI REST API

## Installation/Configuration
The following commands are executed in the terminal.

1. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). 
Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html). 

2. Access the created virtual environment folder

        $ cd your_venv

3. Clone this repository

        $ git clone https://wwwin-github.cisco.com/gve/gve_devnet_aci_ports_usage


4. Access the folder `gve_devnet_aci_ports_usage`

        $ cd gve_devnet_aci_ports_usage

5. Install the dependencies:

        $ pip3 install -r requirements.txt

6. In `.env`, fill out the ACI credentials:

```
base=<https://IP-address/api>
user=<Username>
password=<Password>

```
## Usage
1. To launch the app, type the following command in your terminal:

        $ python3 main.py

2. To access the app, navigate in a browser to `localhost:5010`. The GUI will look like the following: 

![/IMAGES/ACI-ports.png](/IMAGES/ACI-ports.png)

#

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.