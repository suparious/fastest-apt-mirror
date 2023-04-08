import requests
import time
import sys
from operator import itemgetter

def test_mirror_speed(mirror_url):
    package_url = mirror_url + "/dists/stable/main/binary-amd64/Packages.gz"
    start_time = time.time()
    
    try:
        response = requests.get(package_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error testing mirror '{mirror_url}': {e}")
        return sys.maxsize

    elapsed_time = time.time() - start_time
    return elapsed_time

def find_top_mirrors(mirror_list, top_n=3):
    mirror_speeds = []

    for mirror_url in mirror_list:
        elapsed_time = test_mirror_speed(mirror_url)
        mirror_speeds.append((mirror_url, elapsed_time))

    sorted_mirrors = sorted(mirror_speeds, key=itemgetter(1))
    return sorted_mirrors[:top_n]

def main():
    debian_mirrors = [
        "http://ftp.debian.org/debian",
        "http://ftp.ca.debian.org/debian",
        "http://debian.mirror.iweb.ca/debian",
        "http://mirror.csclub.uwaterloo.ca/debian",
        "http://mirror.estone.ca/debian",
        "http://mirror.it.ubc.ca/debian",
        # Add more mirror URLs here
    ]

    top_mirrors = find_top_mirrors(debian_mirrors)

    if top_mirrors:
        print("Top 3 mirrors found:")
        for i, (mirror, response_time) in enumerate(top_mirrors, 1):
            print(f"{i}. {mirror} (response time: {response_time:.2f}s)")
    else:
        print("No valid mirrors found.")

if __name__ == "__main__":
    main()