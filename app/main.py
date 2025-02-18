import logging
from http import HTTPStatus

from fastapi import Depends, FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.config.database import Session, get_db

from app.routes.user import user_routes
from app.routes.department import department_routes
from app.routes.employee import employee_routes

logger = logging.getLogger("fastapi")
app = FastAPI(dependencies=[Depends(get_db)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    db = Session()

    response = {}
    response["server_health"] = "Employee Management System Server API health OK"
    response["database_health"] = "OK" if db.is_active else "disconnected"

    return ORJSONResponse(content=response, status_code=HTTPStatus.OK)


# include routers
app.include_router(user_routes)
app.include_router(department_routes)
app.include_router(employee_routes)
