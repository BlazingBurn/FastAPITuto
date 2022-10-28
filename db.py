from secrets import choice
import databases
import ormar
import sqlalchemy

from Enum.rankenum import Rank

from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Player(ormar.Model):
    class Meta(BaseMeta):
        tablename = "players"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(unique=True, max_length=128, nullable=False)
    level: int = ormar.Integer(unique=True, nullable=False)
    gold: int = ormar.Integer(unique=True, nullable=True)
    rank: str = ormar.String(default=Rank.twig.value, max_length=30, nullable=False, choices=list(Rank))


class Group(ormar.Model):
    class Meta(BaseMeta):
        tablename = "group"
       
    id: int = ormar.Integer(primary_key=True) 
    name: str = ormar.String(unique=True, max_length=128, nullable=False)
    description: str = ormar.String(unique=True, max_length=260, nullable=True)
    powerRank: int = ormar.Integer(unique=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)