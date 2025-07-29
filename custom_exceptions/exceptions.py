import sys

class TripPlannerExceptions(Exception):
    """
    custom class to handle exceptions
    """
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,ext_tb = error_details.exc_info()
        self.lineno = ext_tb.tb_lineno
        self.file_name = ext_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in the python script name {self.file_name} line number {self.lineno} error message {self.error_message}"
    
if __name__ == "__main__":
    try:
        result = 5 /0
        print("Error", result)
    except Exception as e:
        raise TripPlannerExceptions(e, sys)
        
        