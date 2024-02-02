from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import BaseOrm

int_pk = Annotated[int, mapped_column(primary_key=True)]


class ChickenAttributes:
    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f"{self.id} {self.name}"


class Farm(BaseOrm, ChickenAttributes):
    __tablename__ = "farm"
    chickenposts: Mapped[list["ChickenPost"]] = relationship(back_populates="farm")


class House(BaseOrm, ChickenAttributes):
    __tablename__ = "house"
    chickenposts: Mapped[list["ChickenPost"]] = relationship(back_populates="house")


class BreedType(BaseOrm, ChickenAttributes):
    __tablename__ = "breed_type"
    chickenposts: Mapped[list["ChickenPost"]] = relationship(
        back_populates="breed_type"
    )


class Gender(BaseOrm, ChickenAttributes):
    __tablename__ = "gender"
    chickenposts: Mapped[list["ChickenPost"]] = relationship(back_populates="gender")


class ChickenPost(BaseOrm):
    __tablename__ = "chicken_post"

    id: Mapped[int_pk]
    daynum: Mapped[int]
    target_weight: Mapped[float]
    farm_id: Mapped[int] = mapped_column(ForeignKey(Farm.id, ondelete="CASCADE"))
    farm: Mapped["Farm"] = relationship(back_populates="chickenposts")
    house_id: Mapped[int] = mapped_column(ForeignKey(House.id, ondelete="CASCADE"))
    house: Mapped["House"] = relationship(back_populates="chickenposts")
    breed_type_id: Mapped[int] = mapped_column(
        ForeignKey(BreedType.id, ondelete="CASCADE")
    )
    breed_type: Mapped["BreedType"] = relationship(back_populates="chickenposts")
    gender_id: Mapped[int] = mapped_column(ForeignKey(Gender.id, ondelete="CASCADE"))
    gender: Mapped["Gender"] = relationship(back_populates="chickenposts")

    def __repr__(self):
        return f"{self.id} {self.farm} {self.house} {self.breed_type} {self.gender} {self.daynum} {self.target_weight}"
