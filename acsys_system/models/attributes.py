from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute, NumberAttribute, MapAttribute, ListAttribute

class Account(MapAttribute):
    account_ID = NumberAttribute(null=False)
    account_name = UnicodeAttribute(null=False)
    account_height = NumberAttribute(null=False)
    account_weight = NumberAttribute(null=False)
    account_birthday = UTCDateTimeAttribute(null=False)
    account_gender = BooleanAttribute(null=False)
    account_level = NumberAttribute(null=False)
    account_address = UnicodeAttribute(null=False)
    account_pass = UnicodeAttribute(null=False)

class Schedule(MapAttribute):
    account_ID = NumberAttribute(null=False)
    schedule_date = UTCDateTimeAttribute(null=False)
    schedule_time = UTCDateTimeAttribute(null=True)
    circuitmenu_ID = NumberAttribute(null=False)
    calories_burned = NumberAttribute(null=True)
    calories_intake = NumberAttribute(null=True)
    calories_difference = NumberAttribute(null=True)
    ingestion = UnicodeAttribute(null=True)
    training_memory = UnicodeAttribute(null=True)

class Food(MapAttribute):
    food_name = UnicodeAttribute
    food_calorie = NumberAttribute

class Motion(MapAttribute):
    motion_name = UnicodeAttribute
    motion_calorie = NumberAttribute