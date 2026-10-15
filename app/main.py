from fastapi import FastAPI

# Import routers AFTER creating app
from app.routes.health import router as health_router
from app.routes.claim import router as claim_router

# Create FastAPI app instance
app = FastAPI(
    title="Claim Intelligence AI",
    version="0.1.0"
)

# Include routers AFTER app is defined
app.include_router(health_router)
app.include_router(claim_router)