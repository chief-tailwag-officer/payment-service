class ApiException(Exception):

    def __init__(self, message, status):
        super().__init__(message)

        self.status_code = status
        self.error_message = message

    def to_json(self):
        return {
            "status": self.status_code,
            "errorMessage": self.error_message
        }
