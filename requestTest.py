from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


# Basic item
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# Item update
@app.post("/items/")
async def create_item(item: Item):
    item.name = item.name.capitalize()
    
    item_dict = item.dict()
    if item.description:
        description_update = "The price of '" + item.name + "' is " + str(item.price) + " and its description is '" + item.description + "'"
        del item_dict['description']
        item_dict.update({"description": description_update})
    
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Method with path param
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# Method with path and query param
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result