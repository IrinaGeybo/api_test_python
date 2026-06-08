from functools import wraps
from loguru import logger

logger.remove()
logger.add(
    sink=r"C:/Users/Irina/PycharmProjects/api_final/logs",
    level="INFO",
    format="{time:YYYY-MM-DD} | {level} | {message}",
    rotation="10MB",
    retention="10 days"
)

def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__} : {str(e)}")
            raise
    return wrapper