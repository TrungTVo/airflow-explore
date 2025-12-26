from airflow.models import BaseOperator
from airflow.utils.context import Context
import httpx

class GetRequestOperator(BaseOperator):
    """Custom operator to send GET request to provided url"""

    template_fields = ("url",)

    def __init__(self, *, url: str, **kwargs):
        super().__init__(**kwargs)
        self.url = url

    def execute(self, context: Context):
        return httpx.get(self.url).json()