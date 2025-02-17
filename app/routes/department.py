from uuid import UUID

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.serializers.department import DeparmentResponse, DepartmentPost

from app.controllers.department import (
    department_list_controller,
    create_department_controller,
    get_single_department_controller,
    update_department_controller,
    delete_department_controller,
)

router = APIRouter(
    prefix="/departments",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("", tags=["departments"], response_model=list[DeparmentResponse])
async def get_departments(db: Session = Depends(get_db)):
    return await department_list_controller(db)


@router.post("", tags=["departments"], response_model=DeparmentResponse)
async def create_department(payload: DepartmentPost, db: Session = Depends(get_db)):
    return await create_department_controller(payload, db)


@router.get("/{id}", tags=["departments"], response_model=DeparmentResponse)
async def get_single_department(id: int, db: Session = Depends(get_db)):
    return await get_single_department_controller(id, db)


@router.put("/{id}", tags=["departments"], response_model=DeparmentResponse)
async def update_department(
    id: int, payload: DepartmentPost, db: Session = Depends(get_db)
):
    return await update_department_controller(id, payload, db)


@router.delete("/{id}", tags=["departments"])
async def delete_department(id: int, db: Session = Depends(get_db)):
    return await delete_department_controller(id, db)


department_routes = router
