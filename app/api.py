from app import app
from .utils import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)

@app.route('/api/<ip>', methods=['GET'])
def checkip(ip):
    if validate_ip_address(ip):
        response = check_ip(ip)
        if response != False:
            isp_response = check_ISP(ip)
            data = {"IPAdress": ip,
                    "Country": response.country.names['en'],
                    "City": response.continent.names['en'],
                    "Location": str(response.location.longitude) + "," + str(response.location.latitude),
                    "Time_zone": response.location.time_zone,
                    "ISP": isp_response.isp}
            return jsonify(data)
        else:
            data = {"IPAdress": ip,
                    "Country": "",
                    "City": "",
                    "Location": "",
                    "Time_zone": "",
                    "ISP": ""}
            return jsonify(data)
    else:
        data = {"message": "It is not IPAddress"}
        return jsonify(data)

@app.route('/api/proxy/<ip>', methods=['GET'])
def checkipproxy(ip):
    if validate_ip_address(ip):
        proxy = check_proxy(ip)
        if proxy:
            data = {"proxy": "true", "IPAdress": ip}
            return jsonify(data)
        else:
            data = {"proxy": "false", "IPAdress": ip}
            return jsonify(data)
    else:
        data = {"message": "It is not IPAddress"}
        return jsonify(data)