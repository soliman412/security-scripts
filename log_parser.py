from collections import Counter

def parse_failed_logins(path):
    ips = []
    with open(path) as f:
        for line in f:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[parts.index("from") + 1]
                ips.append(ip)
    return Counter(ips)

if __name__ == "__main__":
    result = parse_failed_logins("sample_auth.log")
    for ip, count in result.most_common(5):
        print(f"{ip}: {count} failed attempts")