import geoip2.database
import ipaddress
from pypasser import reCaptchaV3
import requests

def check_ip(ip):
    reader = geoip2.database.Reader("data/GeoIP2-City.mmdb")
    try:
        response = reader.city(ip)
        return response
    except:
        return False

def check_ISP(ip):
    readerISP = geoip2.database.Reader('data/GeoIP2-ISP.mmdb')
    isp_response = readerISP.isp(ip)
    return isp_response


def validate_ip_address(ip_string):
   try:
       ipaddress.ip_address(ip_string)
       return True
   except ValueError:
       return False


def check_proxy(ip):
    url = "https://www.ip2proxy.com/demo"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36'
    }
    recaptcha_response = reCaptchaV3(
        "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfffsgUAAAAAKV3wNc4zq-g5xjmqLQHTaFMCv54&co=aHR0cHM6Ly93d3cuaXAycHJveHkuY29tOjQ0Mw..&hl=en&v=Km9gKuG06He-isPsP6saG8cn&size=invisible&cb=5f75wus5y93m"
    )
    payload = {"ipAddress": ip, "captchaTokenV3": recaptcha_response}
    response = requests.post(url,data=payload, headers=headers).text
    if "This IP address is not a known proxy IP address" in response:
        return False
    else:
        return True
