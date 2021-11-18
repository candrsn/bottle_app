# bottle_app
I am a sample Bottle app to learn about app routing and writing servicing endpoints


## see
(https://bottlepy.org/docs/dev/)

(https://bottlepy.org/docs/dev/routing.html#wildcard-filters)


We have a number of urls that share a prefix

https://www.example.com/app/wiki/<more url parts>

We want to declare an @app.route that will 
* catch those urls with the shared prefix
* compute that new servicing endpoint
* issue a HTTP 303 response with the new computed url


# How to debug - Develop

### use conda to isolate a python env
# and mimic the actual version used in deployment

conda create -n census python==3.6.8
conda activate census_bottle
pip3 install -r requirements.txt



## using vscode to debug

* Open the project dir using the "open Folder" menu

* open the app_server.py file
* set a breakpoint on line 7, inside the hello_world() function
* press f5 to start debugging

* In your browser open the url
    http://127.0.0.1:8080/
* Or use curl to make a request from a command line
    * curl 'http://127.0.0.1:8080/'

* see the app in vscode stop on line 7
   


