"""Script to update local ticker.yaml.

Takes open positions from Fidelity Accounts_History.csv file and overwrites the
configuration file in every case.
"""

from absl import app
from absl import flags
from absl import logging

from ticker_updater import TickerUpdater


FLAGS = flags.FLAGS
flags.DEFINE_string(
    "config",
    "~/.ticker.yaml",
    "`ticker.yaml` file location. Default is `~/.ticker.yaml`.",
)
flags.DEFINE_string(
    "default_config",
    "./default_config.yaml",
    "Default settings file location. Default is `./default_config.yaml`.",
)

logging.set_verbosity(logging.INFO)
logging.get_absl_handler().setFormatter(None)


def main(_):
    updater: TickerUpdater = TickerUpdater(FLAGS.config, FLAGS.default_config)
    updater.run()


if __name__ == "__main__":
    app.run(main)
