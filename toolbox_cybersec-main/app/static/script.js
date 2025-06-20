function getTarget() {
    return document.getElementById("target").value.trim();
}

function sendScanRequest(url) {
    let target = getTarget();
    if (!target) {
        alert("Veuillez entrer une IP ou un domaine !");
        return;
    }

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target: target })
    })
    .then(response => response.json())
    .then(data => {
        const resultBox = document.getElementById("scan_result");
        resultBox.style.display = "block";

        if (data.result) {
            resultBox.innerText = typeof data.result === "string"
                ? data.result
                : JSON.stringify(data.result, null, 2);
        } else if (data.error) {
            resultBox.innerText = "Erreur : " + data.error;
        } else {
            resultBox.innerText = "Aucun résultat.";
        }
    });
}




// Fonctions de scan pour chaque outil

function scanNmap() {
    sendScanRequest("/scan_nmap");
}

function scanUDP() {
    sendScanRequest("/scan_udp");
}

function scanIP() {
    sendScanRequest("/scan_ip");
}

function scanWhois() {
    sendScanRequest("/scan_whois");
}

function scanSubdomains() {
    sendScanRequest("/scan_subdomains");
}

function scanSSL() {
    sendScanRequest("/scan_ssl");
}

function scanTech() {
    sendScanRequest("/scan_tech");
}

function scanVuln() {
    sendScanRequest("/scan_vuln");
}

function scanWAF() {
    sendScanRequest("/scan_waf");
}

function scanBruteforce() {
    sendScanRequest("/scan_bruteforce");
}

function scanSensitiveFiles() {
    sendScanRequest("/scan_sensitive_files");
}

function scanJS() {
    sendScanRequest("/scan_js");
}



function scanHydra() {
    sendScanRequest("/scan_hydra");
}

function scanSQLMap() {
    sendScanRequest("/scan_sqlmap");
}

function scanXSStrike() {
    sendScanRequest("/scan_xsstrike");
}

function scanVolatility() {
    sendScanRequest("/scan_volatility");
}

function scanCuckoo() {
    sendScanRequest("/scan_cuckoo");
}

function scanYara() {
    sendScanRequest("/scan_yara");
}

function scanDirb() {
    sendScanRequest("/scan_dirb");
}

function scanEttercap() {
    sendScanRequest("/scan_ettercap");
}

function scanMetasploit() {
    sendScanRequest("/scan_metasploit");
}



