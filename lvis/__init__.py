import sys
from loguru import logger
from lvis.lvis import LVIS
from lvis.results import LVISResults
from lvis.eval import LVISEval
from lvis.vis import LVISVis


# logger.remove()
loguru_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

# stdout logging:
logger.add(sys.stderr, format=loguru_format)

__all__ = ["LVIS", "LVISResults", "LVISEval", "LVISVis"]
