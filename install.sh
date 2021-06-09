sudo wget https://linux-clients.seafile.com/seafile.asc -O /usr/share/keyrings/seafile-keyring.asc
sudo bash -c "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/seafile-keyring.asc] https://linux-clients.seafile.com/seadrive-deb/bionic/ stable main' > /etc/apt/sources.list.d/seadrive.list"
sudo apt update
sudo apt-get install seadrive-daemon