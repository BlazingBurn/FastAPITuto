from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

# q non required
# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, regex="^fixedquery$", max_length=50, min_length=10)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# q required
@app.get("/items/")
async def read_items(q: str | None = Query(default=..., max_length=50, min_length=4)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# q required => use library Required instead of '...' => weak but easily readable for others
# @app.get("/items/")
# async def read_items(q: str | None = Query(default=Required, max_length=50, min_length=4)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Normal init
# @app.get("/itemsList/")
# async def read_items(q: list[str] | None = Query(default=None)):
#     query_items = {"q": q}
#     return query_items

# Default list
@app.get("/itemsList/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# list don't check type
# @app.get("/itemsList/")
# async def read_items(q: list = Query(default=[])):
#     query_items = {"q": q}
#     return query_items


# title, description, alias, .... the total function but deprecated......
@app.get("/itemsDescriptle/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        title="Best items title ever",
        description="Of course best description like the title",
        min_length=3,
        alias="item-carry",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# This is the best function
@app.get("/itemsDescriptle2/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        title="Best items title ever",
        description="Of course best description like the title",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        alias="item-carry",
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/itemsHidden/")
async def read_items(
    hidden_query: str | None = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}