import subprocess

def print_banner():
    banner = """

     _______. _______   ______ .______        ___        ______  __  ___      ___      .______        ______  __    __  
    /       ||   ____| /      ||   _  \      /   \      /      ||  |/  /     /   \     |   _  \      /      ||  |  |  | 
   |   (----`|  |__   |  ,----'|  |_)  |    /  ^  \    |  ,----'|  '  /     /  ^  \    |  |_)  |    |  ,----'|  |__|  | 
    \   \    |   __|  |  |     |   ___/    /  /_\  \   |  |     |    <     /  /_\  \   |      /     |  |     |   __   | 
.----)   |   |  |____ |  `----.|  |       /  _____  \  |  `----.|  .  \   /  _____  \  |  |\  \----.|  `----.|  |  |  | 
|_______/    |_______| \______|| _|      /__/     \__\  \______||__|\__\ /__/     \__\ | _| `._____| \______||__|  |__| 
                                                                                                                        

    """
    print(banner)

def get_security_tools():
    result = subprocess.run(['pacman', '-Slq'], stdout=subprocess.PIPE)
    if result.returncode != 0:
        print("Error: Unable to fetch package list.")
        return []

    packages = result.stdout.decode('utf-8').splitlines()

    security_keywords = [
        "nmap", "wireshark", "burpsuite", "metasploit", "aircrack-ng", "hydra",
        "sqlmap", "john", "dirbuster", "nessus", "nikto", "gobuster", "ffuf", 
        "snort", "openvas", "impacket", "ettercap", "p0f", "recon-ng", "sparta", 
        "hashcat", "scapy", "wifite", "tshark", "theharvester", "dnsrecon", "dnscan"
    ]

    security_tools = [pkg for pkg in packages if any(keyword in pkg.lower() for keyword in security_keywords)]
    return security_tools

def install_tools(tools):
    for tool in tools:
        print(f"Installing {tool}...")
        subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', tool])

if __name__ == "__main__":
    print_banner()
    print("Listing available cybersecurity tools...")
    security_tools = get_security_tools()

    if security_tools:
        print(f"Found the following tools: {', '.join(security_tools)}")
        install_tools(security_tools)
    else:
        print("No cybersecurity tools found.")
