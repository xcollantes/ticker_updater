# Ticker updater

Updates configuration file for https://github.com/achannarasappa/ticker.

## Getting started

### Installation

For Linux and MacOS:

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
```

### Get Fidelity Account_History.csv file

1. Log into your account
1. Click on `Activities & Orders` tab
1. Select timespan
1. (Optional) For troubleshooting, use `More Filters`
   1. Select `Investment Type > Options`
1. Click on download icon and click on `Download as CSV`

**NOTE:** Be careful with the CSV, this contains your account number.

### Running

```bash
env/bin/python3 update.py \
    --csv [path of csv file]  # Path to output file from Fidelity; default: `Accounts_History.csv`
```

Usage:

```bash
env/bin/python3 update.py \
    --csv ~/Downloads/Accounts_History.csv
```
