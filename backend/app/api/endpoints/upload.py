from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Upload"])

@router.get("/upload/")
async def test():
    return {"message": "Upload endpoint is working."}