from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.IntField(unique=True)
    name = fields.CharField(max_length=100)
    username = fields.CharField(max_length=235)
    age = fields.IntField()
    gender = fields.CharField(max_length=100)
    looking_for = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)
    about = fields.TextField(max_length=225, null=True)
    photo = fields.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name
