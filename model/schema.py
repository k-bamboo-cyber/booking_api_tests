from schema import Schema, And, Use, Optional, SchemaError

schema = Schema([{
    "firstname" : And(str, len),
    "lastname" : And(str, len),
    "totalprice" : And(Use(int), lambda n: 0 <= n),
    "depositpaid" : bool,
    "bookingdates" : {
        "checkin" : full-date,
        "checkout" : full-date"
    },
    Optional("additionalneeds") : str
}])
