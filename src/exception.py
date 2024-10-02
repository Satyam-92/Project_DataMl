import sys
from src.logger import logging  # Assuming logging is properly configured in src.logger

def error_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script [{0}] at line number [{1}] with error message: [{2}]".format(file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Properly initialize the base Exception class
        self.error_message = error_message_details(error, error_detail)
    
    def __str__(self):
        return self.error_message
