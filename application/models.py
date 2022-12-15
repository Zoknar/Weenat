from dataclasses import dataclass, field

from sqlalchemy import Column, DateTime, Float, Integer, String, Table
from sqlalchemy.orm import registry

from . import db

mapper_registry = registry(db.metadata)


@mapper_registry.mapped
@dataclass
class DataRecord:
    """DATA To be requested"""

    __tablename__ = "DataRecord"
    __sa_dataclass_metadata_key__ = "sa"
    id: int = field(
        init=False, metadata={"sa": Column("id", Integer, primary_key=True)}
    )
    datalogger: str = field(metadata={"sa": Column("datalogger", String(30))})
    at: DateTime = field(metadata={"sa": Column("at", DateTime)})
    lat: float = field(metadata={"sa": Column("lat", Float)})
    lng: float = field(metadata={"sa": Column("lng", Float)})
    temp: float = field(metadata={"sa": Column("temp", Float)})
    hum: float = field(metadata={"sa": Column("temp", Float)})
    rain: float = field(metadata={"sa": Column("temp", Float)})
