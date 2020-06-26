from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, ListAttribute
from pynamodb.models import Model
import acsys_system.env as env
from acsys_system.models import attributes

class AccountModel(Model):
    class Meta:
        table_name = "Account"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

        AccountID = NumberAttribute(hash_key=True)
        AccountName = UnicodeAttribute(null=False)
        AccountHeight = NumberAttribute(null=False)
        AccountWeight = NumberAttribute(null=False)
        AccountBirthday = UTCDateTimeAttribute(null=False)
        AccountGender = BooleanAttribute(null=False)
        AccountLevel = NumberAttribute(null=False)
        AccountAddress = UnicodeAttribute(null=False)
        AccountPass = UnicodeAttribute(null=False)

        def __iter__(self):
            for name, attr in self.get_attribute().items():
                yield name, attr.serialize(getattr(self, name))

class ScheduleModel(Model):
    class Meta:
        table_name = "Schedule"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    AccountID = NumberAttribute(hash_key=True)
    ScheduleDate = UTCDateTimeAttribute(null=False)
    ScheduleTime = UTCDateTimeAttribute(null=True)
    CaloriesBurned = NumberAttribute(null=True)
    CaloriesIntake = NumberAttribute(null=True)
    Ingestion = UnicodeAttribute(null=True)
    TrainingMemory = UnicodeAttribute(null=True)

    def __iter__(self):
        for name, attr in self.get_attribute().items():
            yield name, attr.serialize(getattr(self, name))

class FoodModel(Model):
    class Meta:
        table_name = "Food"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    FoodName = UnicodeAttribute(null=False)
    FoodCalorie = NumberAttribute(null=False)

    def __iter__(self):
        for name, attr in self.get_attribute().items():
            yield name, attr.serialize(getattr(self, name))

class MotionModel(Model):
    class Meta:
        table_name = "Motion"
        aws_access_key_id = env.AWS_ACCESS_KEY_ID
        aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY
        region = env.AWS_REGION

    MotionName = UnicodeAttribute(null=False)
    MotionCalorie = NumberAttribute(null=False)

    def __iter__(self):
        for name, attr in self.get_attribute().items():
            yield name, attr.serialize(getattr(self, name))