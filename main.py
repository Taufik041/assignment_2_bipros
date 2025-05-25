from fastapi import FastAPI, status, HTTPException
from schema import employee_data, sort_field
from database import employee_list, save_to_csv

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message":"Homepage"}



@app.get("/employee/{sort_by}", status_code=status.HTTP_200_OK)
def get_employee(sort_by: sort_field):
    sorted_employees = sorted(employee_list, key=lambda x:x[sort_by])
    return sorted_employees



@app.post("/employee/new", status_code=status.HTTP_201_CREATED)
def add_employee(data: employee_data):
    new_employee = dict(data)
    new_employee["id"] = len(employee_list) + 1
    employee_list.append(new_employee)
    save_to_csv()
    raise HTTPException(status_code=status.HTTP_201_CREATED, 
                        detail=f"New employee {new_employee["name"]} added")



@app.post("/employee/{id}", status_code=status.HTTP_202_ACCEPTED)
def edit_employee(id: int, data: employee_data):
    for i, employee in enumerate(employee_list):
        if employee["id"] ==id:
            updated_data = dict(data)
            updated_data["id"] = id
            employee_list[i] = updated_data
            save_to_csv()
            raise HTTPException(status_code=status.HTTP_202_ACCEPTED, 
                                detail=f"Employee with id: {id} updated")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Employee with id: {id} not found")



@app.delete("/employee/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_employee(id: int):
    for i, employee in enumerate(employee_list):
        if employee["id"] ==id:
            deleted = employee_list.pop(i)
            save_to_csv()
            raise HTTPException(status_code=status.HTTP_200_OK, 
                                detail=f"Employee {deleted["name"]} was removed successfully")      
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Employee with id: {id} was not found")