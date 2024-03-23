"""Unit test for ticker_updater.py."""

import unittest
import logging

import yaml

from ticker_updater import TickerUpdater

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestTickerUpdater(unittest.TestCase):
    def test_ticker_updater(self):
        updater = TickerUpdater(
            ticker_config="testdata/test_ticker.yaml",
            default_config="testdata/test_default_config.yaml",
            account_history_path="testdata/test_Accounts_History.csv",
        )
        updater.run()

        # with open("testdata/expected_config.yaml", "r") as expected:
        #     self.assertEqual(updater, yaml.safe_load(expected))
