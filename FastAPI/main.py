from fastapi import FastAPI, HTTPException
from model import Game, Console, GameUpdateRequest
from typing import List
from uuid import uuid4, UUID
import uvicorn

app = FastAPI()

db: List[Game] = [
  Game(
    id=UUID("48bc425d-5386-46fa-a1ba-fbdc6f622b12"),  #keeping the IDs fixed
    game_name="Elden Ring",
    game_developer="FromSoftware Inc",
    url="https://en.bandainamcoent.eu/elden-ring/elden-ring",
    game_size="45 GB",
    release_date="Feb 25, 2022",
    console=[Console.play_station, Console.windows]),
  Game(
    id=UUID("8d7b25c5-508c-43b1-bf12-71001c4ce9f8"),
    game_name="Uncharted: Legacy of Thieves",
    game_developer="Naughty Dog LLC",
    url=
    "https://www.playstation.com/en-ca/games/uncharted-legacy-of-thieves-collection/",
    game_size="126 GB",
    release_date="Jan 28, 2022",
    console=[Console.play_station]),
  Game(
    id=UUID("7a2c6b54-3c28-4d0c-a89e-474ef9fc7739"),  #keeping the IDs fixed
    game_name="Pokémon Legends: Arceus",
    game_developer="Game Freak Co., Ltd",
    url="https://legends.pokemon.com/en-us/",
    game_size="6 GB",
    release_date="Jan 28, 2022",
    console=[Console.nintendo]),
  Game(
    id=UUID("0f76ab39-b08e-423d-9ffe-426f9a50d095"),  #keeping the IDs fixed
    game_name="Core Keeper",
    game_developer="Pugstorm",
    url="https://store.steampowered.com/app/1621690/Core_Keeper/",
    game_size="8 GB",
    release_date="Mar 8, 2022",
    console=[Console.windows]),
]


#get method used to retrieve data from database
@app.get("/api/v1/games")
async def fetch_games():
  return db


#post method is used to submit a new games
@app.post("/api/v1/games")
async def register_game(game: Game):
  db.append(game)
  return {"id": game.id}


#delete method is used to delete a specified game from the list of games
@app.delete("/api/v1/games/{game_id}")
async def delete_game(game_id: UUID):
  for game in db:
    if game.id == game_id:
      db.remove(game)
      return
  #HTTPException is used here for error handling
  raise HTTPException(
    status_code= 404,
    detail=f"game with id: {game_id} does not exist"
  )

#put method is used to update a details of specified game in the list of games
@app.put("/api/v1/games/{game_id}")
async def update_game(game_update: GameUpdateRequest, game_id: UUID):
  for game in db:
    if game.id == game_id:
      if game_update.game_name is not None:
        game.game_name = game_update.update_name
      if game_update.game_developer is not None:
        game.game_developer = game_update.game_developer
      if game_update.url is not None:
        game.url = game_update.url
      if game_update.game_size is not None:
        game.game_size = game_update.game_size
      if game_update.console is not None:
        game.console = game_update.console
      return


#HTTPException is used here for error handling
  raise HTTPException(status_code=404,
                      detail=f"game with id: {game_id} does not exist")
#uvicorn.run(app, host="0.0.0.0", port="8080")
