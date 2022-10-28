from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

pl = [{"id":1,"username":"ThePlayerOne","level":120,"gold":1000000000,"rank":"godLike"},{"id":5,"username":"Boudha","level":49,"gold":1402,"rank":"sharp"},{"id":6,"username":"YakuzaRTT","level":85,"gold":39402,"rank":"warHammer"}]

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    
    strList = []
    for player in pl:
        strList.append(f'Le joueur {player["username"]} possedant l\'id : {player["id"]} est au niveau {player["level"]} et possede le rank de "{player["rank"]}".')
        
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "playerList": strList})