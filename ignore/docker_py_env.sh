# Ensure the email argument is provided
if [ -z "$1" ]; then
  echo "Usage: ./setup.sh your_email@example.com"
  exit 1
fi

EMAIL=$1

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce -y
sudo usermod -aG docker ${USER}
docker build
docker run -it \
    -p 8000:80 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd):/app my-python-env \
    /bin/bash -c "./setup.sh $EMAIL && streamlit run emailapp.py"
