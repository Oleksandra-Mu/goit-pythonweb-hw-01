import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(filename)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
