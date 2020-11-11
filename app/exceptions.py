from werkzeug.exceptions import HTTPException


class WrongValue(HTTPException):
    # TODO: change code
    code = 400
    description = "Wrong value"
