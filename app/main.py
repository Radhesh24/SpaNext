from fastapi import FastAPI
from app.api.v1 import users, salons, bookings

app = FastAPI(title="Salon Booking App")

# Register API routers
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(salons.router, prefix="/api/v1/salons", tags=["Salons"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["Bookings"])
