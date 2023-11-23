from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/random_number/")
async def get_random_number(
    min_number: int = Query(..., title="Minimum Number", description="The minimum number in the range"),
    max_number: int = Query(..., title="Maximum Number", description="The maximum number in the range")):
    try:
        # Validate input parameters
        if min_number >= max_number:
            raise ValueError("Minimum number must be less than the maximum number.")

        # Generate a random number in the specified range
        random_num = random.randint(min_number, max_number)

        return JSONResponse(content={"random_number": random_num}, status_code=200)

    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
