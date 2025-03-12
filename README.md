# Starter code for an API server 

This repository contains example starter code for starting an API server
for the Medra system to interact with. 

This codebase uses Pydantic and FastAPI.

## Requirements 

- Python 3.11+ (A lower version may still work, but requires testing)

## Setup

- Install dependencies with `pip install -r requirements.txt`
- Run the app with `python main.py` or alternatively with Uvicorn `uvicorn main:app`

## Project structure 

- `main.py` - Main API server code
- `medra_response.py` - Example Response objects to send to Medra for special handling

## Instructions

- Modify this starter code however you like 
- Change endpoints and parameter arguments in `main.py` 
- The Medra system can be configured to make POST API calls to this API
  - Send us a copy of the Input Parameter JSON Schema and the API Endpoint path and we'll be able to include this on our Deck's UI as an Action
  - e.g. `/run_instrument`
  -
  - ```json
      {
        "$defs": {
          "PresetEnum": {
            "enum": [
              "normal",
              "rapid",
              "slow"
            ],
            "title": "PresetEnum",
            "type": "string"
          },
          "Well": {
            "properties": {
              "label": {
                "title": "Label",
                "type": "string"
              },
              "id": {
                "maxLength": 20,
                "minLength": 1,
                "title": "Id",
                "type": "string"
              }
            },
            "required": [
              "label",
              "id"
            ],
            "title": "Well",
            "type": "object"
          }
        },
        "properties": {
          "preset": {
            "$ref": "#/$defs/PresetEnum",
            "default": "normal",
            "title": "preset"
          },
          "temperature": {
            "title": "Temperature",
            "type": "number"
          },
          "humidity": {
            "title": "Humidity",
            "type": "number"
          },
          "pressure": {
            "title": "Pressure",
            "type": "number"
          },
          "wells": {
            "items": {
              "$ref": "#/$defs/Well"
            },
            "maxItems": 96,
            "minItems": 1,
            "title": "Wells",
            "type": "array"
          }
        },
        "required": [
          "temperature",
          "humidity",
          "pressure"
        ],
        "title": "InstrumentParams",
        "type": "object"
    }
    ```


## Hardware configuration 

- The instrument that has the REST API is assumed to be on the same 
network as the Medra Deck, whether that be on the same internet network,
or directly plugged into Medra's Deck with a static IP address.
