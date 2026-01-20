# ==============================
# HexaSafeLink - Scam Rules
# ==============================

# Popular shortlink services (Global)
SHORTLINK_DOMAINS = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "buff.ly",
    "cutt.ly", "shorturl.at", "rebrand.ly", "ow.ly", "tiny.cc",
    "s.id", "soo.gd", "shorte.st", "clk.sh"
]

# High-risk TLDs (Worldwide abused)
SUSPICIOUS_TLDS = [
    ".xyz", ".top", ".club", ".online", ".site", ".info", ".biz",
    ".click", ".link", ".live", ".rest", ".cfd", ".loan",
    ".monster", ".work", ".tokyo", ".fit", ".beauty"
]

# Global scam keywords (updated worldwide)
SUSPICIOUS_KEYWORDS = [
    # Money / Reward
    "free", "gift", "offer", "win", "cash", "promo", "reward",
    "bonus", "prize", "claim", "giveaway", "earn", "income",

    # Crypto / Investment
    "bitcoin", "btc", "eth", "crypto", "airdrop", "nft",
    "investment", "trading", "forex", "mining", "profit",

    # Account / Security
    "login", "verify", "verification", "secure", "update",
    "password", "reset", "confirm", "account", "wallet",

    # Urgency / Trap words
    "urgent", "limited", "hurry", "expires", "actnow",
    "click", "clickhere", "unlock", "access",

    # Brand abuse words
    "support", "helpdesk", "service", "customer",
    "bank", "paypal", "facebook", "google", "instagram"
]
