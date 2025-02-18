from uuid import UUID

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.serializers.employee import EmployeeResponse, EmployeePost, EmployeeUpdate

from app.controllers.employee import (
    employee_list_controller,
    create_employee_controller,
    get_single_employee_controller,
    update_employee_controller,
    delete_employee_controller,
)

router = APIRouter(
    prefix="/employees",
    tags=["employee"],
    responses={404: {"description": "Not found"}},
)


@router.get("", tags=["employee"], response_model=list[EmployeeResponse])
async def employee_list(db: Session = Depends(get_db)):
    return await employee_list_controller(db)


@router.post("", tags=["employee"], response_model=EmployeeResponse)
async def create_department(payload: EmployeePost, db: Session = Depends(get_db)):
    return await create_employee_controller(payload, db)


@router.get("/{id}", tags=["employee"], response_model=EmployeeResponse)
async def get_single_employee(id: int, db: Session = Depends(get_db)):
    return await get_single_employee_controller(id, db)


@router.put("/{id}", tags=["employee"], response_model=EmployeeResponse)
async def update_employee(
    id: int, payload: EmployeeUpdate, db: Session = Depends(get_db)
):
    return await update_employee_controller(id, payload, db)


@router.delete("/{id}", tags=["employee"])
async def delete_employee(id: int, db: Session = Depends(get_db)):
    return await delete_employee_controller(id, db)


employee_routes = router
