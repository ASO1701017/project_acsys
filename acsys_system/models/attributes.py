from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, ListAttribute

class AccountAttribute(MapAttribute):
    account_ID = NumberAttribute(null=False)
    account_name = UnicodeAttribute(null=False)
    account_height = NumberAttribute(null=False)
    account_weight = NumberAttribute(null=False)
    account_birthday = UTCDateTimeAttribute(null=False)
    account_gender = BooleanAttribute(null=False)
    account_level = NumberAttribute(null=False)
    account_address = UnicodeAttribute(null=False)
    account_pass = UnicodeAttribute(null=False)

class ScheduleAttribute(MapAttribute):
    account_ID = NumberAttribute(of=AccountAttribute)
    schedule_date = UTCDateTimeAttribute(null=False)
    schedule_time = UTCDateTimeAttribute(null=True)
    calories_burned = NumberAttribute(null=True)
    calories_intake = NumberAttribute(null=True)
    calories_difference = NumberAttribute(null=True)
    ingestion = UnicodeAttribute(null=True)
    training_memory = UnicodeAttribute(null=True)

class FoodAttribute(MapAttribute):
    food_name = UnicodeAttribute(null=False)
    food_calorie = NumberAttribute(null=False)

class MotionAttribute(MapAttribute):
    motion_name = UnicodeAttribute(null=False)
    motion_calorie = NumberAttribute(null=False)