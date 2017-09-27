class ValidationException(Exception):
    def __init__(self, message: str, errors: dict):
        super().__init__(message)
        self.errors = errors

def todo_validator(data: dict) -> dict:
    if not data.get('title'):
        message = "Please provide title"
        raise ValidationException(message, {'title_error': True, "message": message})
    return data
