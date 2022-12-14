from dataclasses import dataclass, field
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import registry

from . import db

mapper_registry = registry(db.metadata)


@mapper_registry.mapped
@dataclass
class Ludo_cpe:
    """Class Représentant un Cpe_ftts, les données viennent de la table ludo_cpe"""

    __tablename__ = "LUDO_CPE"
    __sa_dataclass_metadata_key__ = "sa"
    cpe_name: str = field(
        init=False, metadata={"sa": Column("name", String(40), primary_key=True)}
    )
    site_id: str = field(default=None, metadata={"sa": Column("g2r", String(10))})
    techno: str = field(default=None, metadata={"sa": Column("techno", String(10))})
    debit: str = field(default=None, metadata={"sa": Column(db.String(10))})
    port_speed: str = field(default=None, metadata={"sa": Column(db.String(20))})

    def is_ftts(self):
        """Renvoie True s'il s'agit d'un CPE FTTS"""
        return "-FTTS-" in self.cpe_name
