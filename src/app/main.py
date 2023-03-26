
from app.web.db import disconnect_db
from app.web.health_check import healthcheckcontroller

from app.config.config import get_settings
from sqlalchemy.orm import Session
from flask import Flask



app = Flask(__name__)


if __name__ == '__main__':

    app.run()






# FastAPIInstrumentor.instrument_app(app)

# @app.on_event("startup")
# async def on_startup():
#     print("Customers App started.....")
    


# @app.on_event("shutdown")
# async def shutdown():
#     print("Customers App shutdown....")
#     # await database.disconnect()
#     await disconnect_db()

