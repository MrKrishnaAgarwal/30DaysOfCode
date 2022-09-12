## Requests 

### What is Requests?

Requests is a Python module that you can use to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification. It also allows you to access the response data of Python in the same way.

### Installation

```bash
pip install requests
```

### Usage

```python
import requests

response = requests.get("https://api.github.com/users/MrKrishnaAgarwal")
print(response.json())
```