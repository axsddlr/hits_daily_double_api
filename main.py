import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from api.scraper import HDD

# It's creating an instance of the Limiter class.
limiter = Limiter(key_func=get_remote_address)

# It's creating an instance of the FastAPI class.
app = FastAPI(
    title="Unofficial Hits Daily Double API",
    description="An Unofficial REST API for [Hits Daily Double](https://hitsdailydouble.com/), Made by [Andre "
                "Saddler]( "
                "https://github.com/axsddlr)",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

origins = ["*"]

# It's allowing the API to be accessed from any domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# It's setting the rate limit for the API.
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# It's creating an instance of the HDD class.
hits_dd = HDD()


@app.get("/top50/", tags=["News"])
@limiter.limit("250/minute")
def hits_top_50(request: Request):
    return hits_dd.get_top_50()


if __name__ == "__main__":
    # It's running the app on the host and port specified.
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
