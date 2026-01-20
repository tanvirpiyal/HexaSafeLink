import socket
import tldextract
from hexasafelink.core.rules import (
    SHORTLINK_DOMAINS,
    SUSPICIOUS_TLDS,
    SUSPICIOUS_KEYWORDS
)

def scan_url(url: str):
    findings = []
    risk_score = 0

    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}".lower()
    full_url = url.lower()

    # Shortlink detection
    if domain in SHORTLINK_DOMAINS:
        findings.append("Shortlink detected")
        risk_score += 3

    # Suspicious TLD detection
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            findings.append(f"Suspicious TLD detected ({tld})")
            risk_score += 2

    # Keyword detection
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in full_url:
            findings.append(f"Suspicious keyword detected ({keyword})")
            risk_score += 1

    # DNS Resolve check
    ip_address = None
    try:
        ip_address = socket.gethostbyname(domain)
    except Exception:
        findings.append("DNS resolve failed")
        risk_score += 2

    # Risk Level
    if risk_score >= 7:
        risk_level = "HIGH RISK"
    elif risk_score >= 3:
        risk_level = "SUSPICIOUS"
    else:
        risk_level = "LOW RISK"

    return {
        "domain": domain,
        "ip": ip_address,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "findings": findings
    }
