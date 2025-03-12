"""
This file contains example responses for the Medra NetworkCall action
"""

from typing import Literal
from pydantic import BaseModel, Field


class DataResponse(BaseModel):
    """
    Represents a successful data response, which will be stored as part of the Run's results
    """
    type: Literal["data"] = "data"
    data: str = Field(..., description="The data to return to Medra")

class ErrorResponse(BaseModel):
    """
    Represents an error response, which will be presented to the user to 
    decide to skip/retry
    """
    type: Literal["error"] = "error"
    error: str = Field(..., description="Error message to return to Medra")
    
MedraResponse = DataResponse | ErrorResponse