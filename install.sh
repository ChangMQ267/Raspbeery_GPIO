sudo sed -i 's/\r$//' ./fishManagement_start.sh
sudo chmod +x fishManagement*
sudo cp fishManagement_start.sh /usr/bin/
sudo cp fishManagement.service /etc/systemd/system/