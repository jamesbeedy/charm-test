#! /usr/bin/env python3
"""libraries needed for charm."""
import logging

from ops.charm import CharmBase
from ops.main import main

logger = logging.getLogger()


class TestCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        logger.debug("IN INSTALL HOOK")

if __name__ == "__main__":
    main(TestCharm)
