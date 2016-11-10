from app.app import app, db
from flask_script import Manager
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from resource import (Register, Login, Bucketlists, Bucketlist, Items, Item,
                      Token)

manager = Manager(app)
api = Api(app)
migrate = Migrate(app, db)

api.add_resource(Register, "/auth/register", endpoint="register")
api.add_resource(Login, "/auth/login", endpoint="login")
api.add_resource(Bucketlists, "/bucketlists/", endpoint="bucketlists")
api.add_resource(Bucketlist, "/bucketlists/<id>", endpoint="bucketlist")
api.add_resource(Items, "/bucketlists/<id>/items/", endpoint="items")
api.add_resource(Item, "/bucketlists/<id>/items/<item_id>", endpoint="item")
api.add_resource(Token, "/token", endpoint="token")


manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
