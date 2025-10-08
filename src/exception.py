import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

'''
Step by step:

    error_detail.exc_info()

    Returns a tuple (type, value, traceback) of the current exception.

    _ , _, exc_tb → We ignore type and value and only keep traceback.

    exc_tb.tb_frame.f_code.co_filename

    From the traceback object, we get the file name where the exception occurred.

    exc_tb.tb_lineno

    Gets the line number where the exception occurred.

    str(error)

    Converts the exception object to a string to get the error message.

    Combine all into a formatted string:


'''
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        