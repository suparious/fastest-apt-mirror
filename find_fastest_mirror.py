import requests
import time
import sys
import json
from operator import itemgetter

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def test_mirror_speed(mirror_url, package_path):
    package_url = mirror_url + package_path
    start_time = time.time()
    
    try:
        response = requests.get(package_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error testing mirror '{mirror_url}': {e}")
        return sys.maxsize

    elapsed_time = time.time() - start_time
    return elapsed_time

def find_top_mirrors(mirror_list, package_path, top_n=3):
    mirror_speeds = []

    for mirror_url in mirror_list:
        elapsed_time = test_mirror_speed(mirror_url, package_path)
        mirror_speeds.append((mirror_url, elapsed_time))

    sorted_mirrors = sorted(mirror_speeds, key=itemgetter(1))
    return sorted_mirrors[:top_n]

def main():
    config = load_config()

    # Change this to "ubuntu" for testing Ubuntu mirrors
    distro = "debian"

    mirrors = config[distro]["mirrors"]
    package_path = config[distro]["package_path"]

    top_mirrors = find_top_mirrors(mirrors, package_path)

    if top_mirrors:
        print(f"Top 3 mirrors for {distro.capitalize()} found:")
        for i, (mirror, response_time) in enumerate(top_mirrors, 1):
            print(f"{i}. {mirror} (response time: {response_time:.2f}s)")
    else:
        print("No valid mirrors found.")

if __name__ == "__main__":
    main()
