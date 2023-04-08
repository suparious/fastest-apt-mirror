import requests
import time
import sys

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

def find_fastest_mirror(mirror_list):
    fastest_mirror = None
    min_time = sys.maxsize

    for mirror_url in mirror_list:
        elapsed_time = test_mirror_speed(mirror_url)
        
        if elapsed_time < min_time:
            min_time = elapsed_time
            fastest_mirror = mirror_url

    return fastest_mirror, min_time

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

    fastest_mirror, min_time = find_fastest_mirror(debian_mirrors)

    if fastest_mirror:
        print(f"Fastest mirror found: {fastest_mirror} (response time: {min_time:.2f}s)")
    else:
        print("No valid mirrors found.")

if __name__ == "__main__":
    main()
