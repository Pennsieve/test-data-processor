import os
import uuid

class Config:
    def __init__(self):
        self.ENVIRONMENT          = os.getenv('ENVIRONMENT', 'local')

        if self.ENVIRONMENT == 'local':
            self.INPUT_DIR            = os.getenv('INPUT_DIR')
            self.OUTPUT_DIR           = os.getenv('OUTPUT_DIR')
        else:
            # workflow / analysis pipeline only supports 3 processors (pre-, main, post-)
            # the output directory of the main processor is what the post-processor needs to read from
            # so for now we will set the input directory for this processor to be the output directory variable
            self.INPUT_DIR            = os.getenv('OUTPUT_DIR')
            self.OUTPUT_DIR           = os.path.join(self.INPUT_DIR, "output")
            if not os.path.exists(self.OUTPUT_DIR):
                os.makedirs(self.OUTPUT_DIR)

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
