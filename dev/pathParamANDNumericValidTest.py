from fastapi import FastAPI, Path, Query

app = FastAPI()

# First version decla
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: str | None = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Second version decla
# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Third version decla
@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get", ge=1, le=1000), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results