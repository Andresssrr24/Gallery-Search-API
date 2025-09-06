from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Search"])

@router.get("/search/")
async def test():
    return {"message": "Searching endpoint is working."}