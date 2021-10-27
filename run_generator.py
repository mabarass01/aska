import os
os.system("apt-get install -y unzip wget openssh-server && wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip && mv ./ngrok /usr/bin/ngrok && service ssh start")
os.system("ngrok authtoken 1pTJd3HRqdzzZPwHIWGSkrgEtLN_41A7CQFfeAKcnHa2ShxoX")
os.system("ngrok tcp 22")
