from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field
from Enum.rankenum import Rank
from db import database, Player, Group


app = FastAPI(title="FastAPI, Docker, and Traefik")

# class Player(BaseModel):
#     id: int
#     username: str
#     level: int 
#     gold: int | None = None
#     rank: Rank
    

# class Group(BaseModel):
#     name: str
#     description: str | None = None
#     powerRank: int


# ---------------------------- BASIC SET UP ----------------------------

@app.get("/")
async def read_root():
    return await Player.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await Player.objects.get_or_create(username="ThePlayerOne", level=120, gold=1000000000, rank=Rank.godLike.value) 
    await Player.objects.get_or_create(username="Boudha", level=49, gold=1402, rank=Rank.sharp.value)
    await Player.objects.get_or_create(username="YakuzaRTT", level=85, gold=39402, rank=Rank.warHammer.value) 
    await Group.objects.get_or_create(name="OneForAll", description="Join if you want to be the GOAT", powerRank=1)

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

# # ---------------------------- GET METHOD ----------------------------

# # player list
# @app.get("/player/")
# async def read_player(q: list[str] = Query(default=["player1", "player2"])):
#     query_items = {"q": q}
#     return query_items

# # group list
# @app.get("/group/")
# async def read_group(q: list[str] = Query(default=["group1", "group2"])):
#     query_items = {"q": q}
#     return query_items

# # This is the best function
# @app.get("/player/{player_id}")
# async def read_player(
#     q: str
#     | None = Query(
#         default=None,
#         title="Best items title ever",
#         description="Of course best description like the title",
#         min_length=3,
#         max_length=50,
#         alias="player",
#     )
# ):
#     results = {"items": [{"item_id": "playerInfo"}]}
#     if q:
#         results.update({"q": q})
#     return results



# # ---------------------------- POST METHOD ----------------------------

# # Player update
# @app.post("/player/")
# async def create_player(player: Player):
#     player.username = player.username.capitalize()
    
#     player_dict = player.dict()
#     if player.gold:
#         gold_update = "The player '" + player.username + "' had " + str(player.gold) + "."
#         del player_dict['gold']
#         player_dict.update({"gold": gold_update})
    
#     return player_dict

# # Group update
# @app.post("/group/")
# async def create_group(group: Group):
#     group.name = group.name.capitalize()
    
#     group_dict = group.dict()
#     if group.description:
#         description_update = "The group '" + group.name + "' had a description " + group.description + "."
#         del group_dict['description']
#         group_dict.update({"description": description_update})
    
#     return group_dict



# # ---------------------------- PUT METHOD ----------------------------

# # use Body
# @app.put("/player/{player_id}")
# async def update_player(player_id: int, player: Player, importance: int = Body()):
#     results = {"player_id": player_id, "player": player, "importance": importance}
#     return results

# @app.put("/group/{group_id}")
# async def update_group(group_id: int, group: Group, importance: int = Body()):
#     results = {"group_id": group_id, "group": group, "importance": importance}
#     return results
