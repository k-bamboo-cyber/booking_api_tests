import pytest

from model.booking import BookingData
from model.schema import post_booking_schema, is_validate


class TestGetBookingIds:
    def test_create_new_booking(self, client):
        """
        1. Add new booking
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.skip("Ошибка в апи, приходит 500")
    @pytest.mark.parametrize(
        "field,value", [("firstname", 21), ("lastname", 34), ("additionalneeds", 45)]
    )
    def test_create_invalid_booking(self, field, value, client):
        """
        1. Add new booking with invalid params
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.parametrize(
        "field,value", [("firstname", ""), ("lastname", ""), ("additionalneeds", "")]
    )
    def test_create_booking_with_empty_params(self, field, value, client):
        """
        1. Add new booking with empty params
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.parametrize(
        "field,value",
        [("totalprice", 100000), ("totalprice", 0), ("totalprice", 10000000000)],
    )
    def test_create_booking_with_valid_totalprice(self, field, value, client):
        """
        1. Add new booking with valid totalprice
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.xfail(reason="происходит " "округление в меньшую сторону")
    @pytest.mark.parametrize(
        "field,value",
        [("totalprice", -4), ("totalprice", 22344.455), ("totalprice", 0.001)],
    )
    def test_create_booking_invalid_totalprice(self, field, value, client):
        """
        1. Add new booking with invalid totalprice
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.xfail(reason="Принимает только True/False")
    @pytest.mark.parametrize("field,value", [("depositpaid", ""), ("depositpaid", "Y")])
    def test_create_booking_invalid_depositpaid(self, field, value, client):
        """
        1. Add new booking with invalid depositpaid
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.parametrize("checkin,checkout", [("2017-07-24", "2017-07-24")])
    def test_create_booking_same_checkdates(self, checkin, checkout, client):
        """
        1. Add new booking with same checkdates
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        data.bookingdates.checkin = checkin
        data.bookingdates.checkout = checkout
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    @pytest.mark.parametrize(
        "checkin,checkout",
        [pytest.param("", "", marks=pytest.mark.xfail), ("2012-07-24", "2017-07-24")],
    )
    def test_create_booking_invalid_checkdates(self, checkin, checkout, client):
        """
        1. Add new booking with invalid checkdates
        2. Check data and status
        3. Validate schema
        """

        data = BookingData().random()
        data.bookingdates.checkin = checkin
        data.bookingdates.checkout = checkout
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"

    def test_create_same_booking(self, client):
        """
        1. Add new booking
        2. Add the same booking
        3. Check data and status
        4. Validate schema
        """

        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get("booking") == data
        res1 = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res1.json()
        assert booking_info.get("booking") == data
        assert is_validate(booking_info, post_booking_schema), "Check booking schema"
