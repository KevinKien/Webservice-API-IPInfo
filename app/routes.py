from app import app, csrf
from .utils import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ip = request.form['IPAddress']
        if validate_ip_address(ip):
            response = check_ip(ip)
            proxy = check_proxy(ip)
            if response != False:
                isp_response = check_ISP(ip)
                Country = response.country.names['en']
                City = response.continent.names['en']
                Location = "%s,%s" % (str(response.location.longitude), str(response.location.latitude))
                Time_zone = response.location.time_zone
                ISP = isp_response.isp
                return render_template("home.html", ip=ip, Country=Country, City=City, Location=Location, Time_zone=Time_zone, ISP=ISP, Proxy=proxy)
            else:
                return render_template("home.html", ip=ip, Country="", City="", Location="", Time_zone="", ISP="", Proxy=proxy)
        else:
            return render_template("home.html", ip=ip, Country="", City="", Location="", Time_zone="", ISP="", Proxy=proxy)
    else:
        ip = request.remote_addr
        if validate_ip_address(ip):
            response = check_ip(ip)
            proxy = check_proxy(ip)
            if response != False:
                isp_response = check_ISP(ip)
                Country = response.country.names['en']
                City = response.continent.names['en']
                Location = str(response.location.longitude) + "," + str(response.location.latitude)
                Time_zone = response.location.time_zone
                ISP = isp_response.isp
                return render_template("home.html", ip=ip, Country=Country, City=City, Location=Location, Time_zone=Time_zone, ISP=ISP)
            else:
                return render_template("home.html", ip=ip, Country="", City="", Location="", Time_zone="", ISP="", Proxy=proxy)
        else:
            return render_template("home.html", ip=ip, Country="", City="", Location="", Time_zone="", ISP="", Proxy=proxy)