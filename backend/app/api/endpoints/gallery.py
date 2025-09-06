from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Gallery"])

@router.get("/gallery/")
async def test():
    return {"message": "Gallery endpoint is working."}