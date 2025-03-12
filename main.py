from enum import Enum
from fastapi import FastAPI 
from pydantic import BaseModel, Field
import json

from medra_response import DataResponse, ErrorResponse, MedraResponse

app = FastAPI() 

class PresetEnum(str, Enum):
    normal = "normal"
    high = "rapid"
    low = "slow"

class Well(BaseModel):
    label: str
    id: str = Field(..., min_length=1, max_length=20)

class InstrumentParams(BaseModel):
    preset: PresetEnum = Field(title="preset", default=PresetEnum.normal)
    temperature: float
    humidity: float
    pressure: float
    wells: list[Well] = Field(..., default_factory=list, min_length=1, max_length=96)

app = FastAPI()

@app.post("/run_instrument", response_model=MedraResponse)
def run_instrument(params: InstrumentParams):
    # Simulate running the instrument with the provided parameters
    print(f"Running instrument with params: {params}")
    
    return DataResponse(data="Instrument run successfully")
    
@app.post("/mock_failure", response_model=MedraResponse)
def mock_equipment_failure():
    return ErrorResponse(error="Something went wrong with the equipment")

print(json.dumps(InstrumentParams.model_json_schema(), indent=2))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)