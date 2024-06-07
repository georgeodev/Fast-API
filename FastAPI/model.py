#pydantic is a python library to perform data validation
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


#enum to hold a list of operating systems
class Console(str, Enum):
  play_station = "Play Station"
  windows = "Windows PC"
  nintendo = "Nintendo"


#class to manage the game dataset
class Game(BaseModel):
  id: Optional[UUID] = uuid4()  #this is to get a uuid if it is not provided
  game_name: str
  game_developer: str
  url: str
  game_size: Optional[str]
  release_date: str
  console: List[Console]


#class used to implement the update method for the game
class GameUpdateRequest(BaseModel):
  game_name: Optional[str]
  game_developer: Optional[str]
  url: Optional[str]
  game_size: Optional[str]
  console: Optional[List[Console]]
