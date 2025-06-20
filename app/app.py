from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Importer les outils
from pentest.nmap_scan import scan_ports
from pentest.whois_scan import whois_lookup

from pentest.ssl_scan import scan_ssl
from pentest.tech_scan import detect_technologies
from pentest.vuln_scan import scan_vulnerabilities
from pentest.sensitive_files import find_sensitive_files
from pentest.ip_lookup import get_ips
from pentest.bruteforce import bruteforce_login
from pentest.waf_detection import detect_waf
from pentest.js_finder import find_js_files
from pentest.metasploit_scan import metasploit_scan
from pentest.ettercap_scan import run_ettercap
from pentest.volatility_scan import run_volatility
from pentest.cuckoo_scan import run_cuckoo_scan
from pentest.yara_scan import run_yara
from pentest.sqlmap_scan import run_sqlmap
from pentest.xss_scan import run_xss_scan
from pentest.gobuster_scan import run_gobuster_scan






app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')  # Charge la page HTML

# 🔹 API Scan Nmap
@app.route('/scan_nmap', methods=['POST'])
def api_scan_nmap():
    data = request.json
    return jsonify(scan_ports(data.get("target")))

# 🔹 API WHOIS
@app.route('/scan_whois', methods=['POST'])
def api_scan_whois():
    data = request.json
    return jsonify(whois_lookup(data.get("target")))

@app.route('/scan_dirs', methods=['POST'])
def scan_dirs():
    data = request.get_json()
    target = data.get('target')
    return jsonify(run_gobuster_scan(target))




# 🔹 API Scan SSL
@app.route('/scan_ssl', methods=['POST'])
def api_scan_ssl():
    data = request.json
    return jsonify(scan_ssl(data.get("target")))

# 🔹 API Détection de technologies
@app.route('/scan_tech', methods=['POST'])
def api_scan_tech():
    data = request.json
    return jsonify(detect_technologies(data.get("target")))

# 🔹 API Scan de vulnérabilités
@app.route('/scan_vuln', methods=['POST'])
def api_scan_vuln():
    data = request.json
    return jsonify(scan_vulnerabilities(data.get("target")))

@app.route('/scan_sensitive_files', methods=['POST'])
def api_scan_sensitive_files():
    data = request.json
    return jsonify(find_sensitive_files(data.get("target")))

@app.route('/scan_ip', methods=['POST'])
def api_scan_ip():
    data = request.json
    return jsonify(get_ips(data.get("target")))

from flask import Response
import json

@app.route('/scan_bruteforce', methods=['POST'])
def api_scan_bruteforce():
    data = request.json
    target = data.get("target")
    result = bruteforce_login(target)

    # Encodage JSON avec les bons retours ligne
    return Response(
        response=json.dumps({"result": result}),
        status=200,
        mimetype="application/json"
    )




@app.route('/scan_waf', methods=['POST'])
def api_scan_waf():
    data = request.json
    return jsonify(detect_waf(data.get("target")))

@app.route('/scan_js', methods=['POST'])
def api_scan_js():
    data = request.json
    return jsonify(find_js_files(data.get("target")))


@app.route('/scan_metasploit', methods=['POST'])
def api_scan_metasploit():
    data = request.json
    return jsonify(metasploit_scan(data.get("target")))

@app.route('/scan_ettercap', methods=['POST'])
def api_scan_ettercap():
    data = request.json
    return jsonify(run_ettercap(data.get("interface")))


@app.route('/scan_volatility', methods=['POST'])
def api_volatility():
    data = request.json
    return jsonify(run_volatility(data.get("image_path"), data.get("plugin")))

@app.route('/scan_cuckoo', methods=['POST'])
def api_cuckoo():
    data = request.json
    return jsonify(run_cuckoo_scan(data.get("file_path")))

@app.route('/scan_yara', methods=['POST'])
def api_yara():
    data = request.json
    return jsonify(run_yara(data.get("rule_path"), data.get("file_path")))

@app.route('/scan_sqlmap', methods=['POST'])
def api_sqlmap():
    data = request.json
    return jsonify(run_sqlmap(data.get("target")))

@app.route('/scan_xss', methods=['POST'])
def api_xss():
    data = request.json
    return jsonify(run_xss_scan(data.get("target")))




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
