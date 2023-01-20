# SSRF Redirector
A simple Flask system to test SSRF redirect vulnerabilities in web applications.

## Installation
1. Clone the repository
2. Install the requirements; `pip install -r requirements.txt`
3. Run the application; `python app.py`
4. Use `localhost.run` to expose the application to the internet; `ssh -R 80:localhost:5000 localhost.run`
5. Use the exposed URL to test SSRF vulnerabilities

## Usage
1. Use the exposed URL to test SSRF vulnerabilities 
2. Grab the request data from the server
3. Use the request data to exploit the vulnerability

> Change redirections by editing the `receive` function in `app.py`

## Credits
- @sushilphuyal; https://github.com/sushilphuyal
- @basant0x01; https://github.com/sushilphuyal
