#! /usr/bin/env python3
"""libraries needed for charm."""
import json
import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import (
    ActiveStatus,
    BlockedStatus,
)
from ops.framework import StoredState
from slurm_ops_manager import SlurmOpsManager

from slurmd_provides import SlurmdProvides

logger = logging.getLogger()


class SlurmdCharm(CharmBase):
    """Operator charm responsible for coordinating lifecycle operations for slurmd."""
    _stored = StoredState()
    def __init__(self, *args):
        """Initialize charm, configure states, and events to observe."""
        super().__init__(*args)
        self.config = self.model.config
        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        logger.debug("IN INSTALL HOOK")

if __name__ == "__main__":
    main(SlurmdCharm)
