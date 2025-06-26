from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_salon():
    return {"message": "Salon route is working"}
