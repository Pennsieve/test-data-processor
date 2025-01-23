import os
import uuid

class Config:
    def __init__(self):
        self.ENVIRONMENT          = os.getenv('ENVIRONMENT', 'local')

        self.INPUT_DIR            = os.getenv('INPUT_DIR')
        self.OUTPUT_DIR           = os.getenv('OUTPUT_DIR')

        # continue to use INTEGRATION_ID environment variable until runner
        # has been converted to use  a different variable to represent the workflow instance ID
        self.WORKFLOW_INSTANCE_ID = os.getenv('INTEGRATION_ID', str(uuid.uuid4()))

        self.API_KEY              = os.getenv('PENNSIEVE_API_KEY')
        self.API_SECRET           = os.getenv('PENNSIEVE_API_SECRET')
        self.API_HOST             = os.getenv('PENNSIEVE_API_HOST', 'https://api.pennsieve.net')
        self.API_HOST2            = os.getenv('PENNSIEVE_API_HOST2', 'https://api2.pennsieve.net')

        self.FUNCTION             = os.getenv('FUNCTION', 'none')
        self.OPERATOR             = os.getenv('OPERATOR')
        self.OPERAND              = os.getenv('OPERAND')

    def __str__(self):
        return f"ENVIRONMENT: {self.ENVIRONMENT} INPUT_DIR: {self.INPUT_DIR} OUTPUT_DIR: {self.OUTPUT_DIR} " + \
                f"WORKFLOW_INSTANCE_ID: {self.WORKFLOW_INSTANCE_ID} " + \
                f"API_KEY: {self.API_KEY} API_SECRET: {self.API_SECRET} API_HOST: {self.API_HOST} " + \
                f"API_HOST2: {self.API_HOST2} " + \
                f"FUNCTION: {self.FUNCTION} OPERATOR: {self.OPERATOR} OPERAND: {self.OPERAND}"

