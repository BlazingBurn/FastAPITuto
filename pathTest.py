from fastapi import FastAPI

app = FastAPI()

# test first path param => return param from path
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# test item_id for int
# if path param int => return param with format int if not a valid integer return error (example string, float, ect...)
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}