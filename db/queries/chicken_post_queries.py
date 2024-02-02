from typing import List, Dict

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from tqdm import tqdm

from db.database import session_fact
from db.models import Farm, BreedType, Gender, House, ChickenPost


def create_or_get_chicken_attribute(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
        return instance


def insert_chicken_post_from_csv(csv_data: List[Dict]) -> None:
    with session_fact() as session:
        for index in tqdm(range(len(csv_data))):
            attributes = {}
            for attribute_model in [Farm, BreedType, Gender, House]:
                name = csv_data[index][attribute_model.__tablename__]
                obj = create_or_get_chicken_attribute(
                    session=session, model=attribute_model, name=name
                )
                attributes[attribute_model.__tablename__] = obj

            post = ChickenPost(
                daynum=int(csv_data[index]["daynum"]),
                target_weight=float(csv_data[index]["target_weight"]),
                farm=attributes["farm"],
                breed_type=attributes["breed_type"],
                gender=attributes["gender"],
                house=attributes["house"],
            )
            session.add(post)
            session.flush()
        session.commit()


def select_chicken_posts() -> list[ChickenPost]:
    with session_fact() as session:
        query = select(ChickenPost).options(
            joinedload(ChickenPost.farm),
            joinedload(ChickenPost.house),
            joinedload(ChickenPost.breed_type),
            joinedload(ChickenPost.gender),
        )
        res = session.execute(query)
        result = res.unique().scalars().all()
        return result
