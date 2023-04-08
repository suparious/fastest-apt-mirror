# Fastest Mirror Finder

This Python script helps you find the fastest Debian or Ubuntu mirror by testing the response time of a list of mirrors. The script is configurable and allows you to test mirrors for different distributions without modifying the main script. It also provides a progress animation during testing, making it user-friendly and informative.

## Requirements

Python 3
- requests
- argparse
- tqdm

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastest-mirror-finder.git
```

2. Change to the project directory:

```bash
cd fastest-mirror-finder
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```


## Usage

1. Configure the mirrors and package paths for the desired distributions in `config.json`. The default configuration includes Debian and Ubuntu mirrors.

2. Run the script without arguments to test the mirrors for the first distribution found in `config.json`:

```bash
python find_fastest_mirror.py
```

3. To test the mirrors for a specific distribution, use the `-d` or `--distro` option followed by the distribution name:

```bash
python find_fastest_mirror.py -d ubuntu
```


4. The script will display the top 3 mirrors with the fastest response times.

## Customization

- To add or modify mirrors for a specific distribution, edit the `config.json` file.

- To change the number of top mirrors displayed, modify the `top_n` argument in the `find_top_mirrors` function call in the `main` function.

## Contributing

1. Fork the project repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes to the new branch.
4. Submit a pull request with a description of your changes.

## License

This project is licensed under the [GNU General Public License](LICENSE).
