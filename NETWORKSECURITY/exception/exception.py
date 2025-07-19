import sys
import traceback
from NETWORKSECURITY.logging import logger # assuming you have a logging setup here

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message

        # Get traceback details
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in Python script [{self.filename}] at line [{self.lineno}]: {str(self.error_message)}"
if __name__ == '__main__':
    try:
        logger.logging.info("Entering the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
