"""Class ticker updater."""

import yaml
import pandas as pd
from absl import logging


class TickerUpdater:
    def __init__(
        self, ticker_config: str, default_config: str, account_history_path: str
    ) -> None:
        self.ticker_config = ticker_config
        self.default_config = default_config
        self.account_history_path = account_history_path
        self.default: yaml.YAMLObject = yaml.YAMLObject()

    def run(self) -> None:
        """Save file."""
        self.default: yaml.YAMLObject = self._read_default_config()
        self._parse_account_file()

    def _parse_account_file(self) -> pd.DataFrame:
        """Read account file."""
        df = pd.read_csv(self.account_history_path)[
            ["Symbol", "Action", "Quantity", "Price ($)"]
        ].dropna()

        df["Action"] = df["Action"].astype(str)
        df["Quantity"] = df["Quantity"].astype(int)
        df["Price ($)"] = df["Price ($)"].astype(float)

        df["Action"] = df["Action"].apply(lambda d: "BUY" if "BOUGHT" in d else "SELL")

        return df

    def _read_default_config(self) -> yaml.YAMLObject:
        """Read default config file."""
        logging.info("Reading default configuration file: %s", self.default_config)
        with open(self.default_config, "r") as file:
            return yaml.safe_load(file)

    def get_open_positions(self) -> pd.DataFrame:
        """Parse account file and get DataFrame of open positions."""
        history_df: pd.DataFrame = self._parse_account_file()
        grouped = history_df.groupby(["Symbol"])

        

    def _write_out(self, path: str) -> None:
        """Write file."""
        logging.info("Overwriting file")
        with open(path, "w") as file:
            file.write("hello world")
