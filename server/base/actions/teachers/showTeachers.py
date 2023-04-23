from server.base.connect import db


async def show_teachers():
    res = db["Teachers"].find({})
    tab = []
    async for i in res:
        tab.append(i)

    return tab
