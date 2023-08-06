import sys
import logger

def error_message_detail(error, error_detail: sys):
    _,_, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python code: [{0}] line# [{1}] Error: [{2}]".format(file_name, exec_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message

if __name__ == "__main__":
    try:
        result = 1/ 0
    except Exception as ex:
        logger.logging.info(ex)
        raise CustomException(ex, sys)
    