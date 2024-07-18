from models import async_session
from models import Table
from sqlalchemy import select



async def set_point(tg_id, description):
    async with async_session() as session:
        point = await session.scalar(select(Table).where(Table.tg_id == tg_id, Table.description == description))

        if not point:
            session.add(Table(tg_id=tg_id, description=description))
            await session.commit()


async def get_descrip(tg_id):
    async with async_session() as session:
        return await session.scalars(select(Table).where(Table.tg_id == tg_id))



