import json

from schema import Schema, SchemaError

post_booking_schema = Schema(
    {
        "bookingid": int,
        "booking": {
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": bool,
            "bookingdates": {
                "checkin": str,
                "checkout": str,
            },
            "additionalneeds": str,
        },
    }
)

get_booking_schema = Schema(
    {
        "firstname": str,
        "lastname": str,
        "totalprice": int,
        "depositpaid": bool,
        "bookingdates": {
            "checkin": str,
            "checkout": str,
        },
        "additionalneeds": str,
    }
)


def is_validate(data: dict, schema: Schema) -> bool:
    """
    Validate json schema
    :return: True if validation is successful else False
    """
    try:
        data = json.loads(json.dumps(data, default=lambda o: o.__dict__))
        schema.validate(data)
        return True
    except SchemaError:
        return False
