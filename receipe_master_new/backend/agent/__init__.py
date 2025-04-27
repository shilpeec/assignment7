# agent/__init__.py
from .perception import embed_query
from .memory import search_faiss
from .action import fallback_to_llm

# Optionally, you could log initialization or set constants
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("Agent package initialized.")
