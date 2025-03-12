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

## Hardware configuration 

- The instrument that has the REST API is assumed to be on the same 
network as the Medra Deck, whether that be on the same internet network,
or directly plugged into Medra's Deck with a static IP address.