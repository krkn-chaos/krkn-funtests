import requests


def make_http_request(url):
    try:
        response = requests.get(url, timeout=1)
        return "success", response.status_code
    except requests.exceptions.ConnectionError as e:
        return "no_such_host", 404
    except requests.exceptions.Timeout as e:
        return "timeout", 408
    except requests.exceptions.RequestException as e:
        return "error", 500
