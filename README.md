# Introduction
This repository aims to support the reproducibility of the tests conducted and presented in the paper titled 'QUIC and WebSocket for Secure and Low-Latency IoT Communications: an Experimental Analysis,' which was presented at the IEEE International Conference on Communications, held from May 28th to June 1st, 2023, in Rome, Italy.
The demo presented here is based on modified scripts from the [aioquic](https://github.com/aiortc/aioquic) library, customized to meet our needs of establishing communication between IoT nodes and evaluating data transfer performance.

# Running the demo
To execute this script, you will need to have Python 3.7 or a later version installed on your computer. Additionally, you will need to install all the required libraries beforehand.

```console
pip install aioquic asgiref dnslib "flask<2.2" httpbin starlette "werkzeug<2.1" wsproto
```

After executing the following command, simply follow the on-screen instructions to initiate the communication between the Client and Server using WebSocket over QUIC.

```console
python main.py
```
