Steps to run the application

Download or clone the repository to your local machine

open the directory in vscode or using command prompt

once opened in vscode add new terminal
split the terminal into two

in first terminal do following steps:
1.change directory to flask-server:
cd flask-server

2.make virtual enivornment using command :-
pip install virtualenv
virtualenv myenv
myenv\Scripts\activate

3.install required modules:
pip install -r requirements.txt

4.Run the flask app:
python app.py

5.open the browser and open localhost:5000 to view proxy server

in second terminal
1.change directory to client
cd client

2.use the following two commads to run react app
npm install -g serve
serve -s build

3.open web browser and open localhost:3000
here you can upload data file and get filtered data
