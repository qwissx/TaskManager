from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):

    def __init__(self, status_code = status.HTTP_404_NOT_FOUND, detail = "User was not found"):
        super().__init__(status_code, detail)


class ProfileNotFoundException(HTTPException):
    
    def __init__(self, status_code = status.HTTP_404_NOT_FOUND, detail = "Profile was not found"):
        super().__init__(status_code, detail)


class TaskNotFoundException(HTTPException):

    def __init__(self, status_code = status.HTTP_404_NOT_FOUND, detail = "Task was not found"):
        super().__init__(status_code, detail)