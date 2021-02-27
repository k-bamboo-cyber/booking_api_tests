import pytest

from model.schema import schema


class TestGetBooking:

    def test_get_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(id_booking)
        assert res.json() == create_booking.get('booking')

    @pytest.mark.xfail(reason="принимает пустой айди")
    def test_get_booking_empty_id(self, client, create_booking):
        """
           1. Add new booking
           2. Search booking by empty id
           3. Check data and status
           4. Validate schema
        """
        res = client.get_booking('')
        assert res.status_code == 404
        assert schema.validate(res.json()) == create_booking.get('booking')

    @pytest.mark.xfail(reason="несуществующий айди")
    def test_get_booking_nonexist_id(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Take non-exist booking
           4. Check data and status
           5. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(int(id_booking) + 100000)
        assert res.status_code == 404
        assert schema.validate(res.json()) == create_booking.get('booking')

    @pytest.mark.xfail(reason="200 при айди строкой")
    def test_get_booking_by_string_id(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Take booking by string id
           4. Check data and status
           5. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(str(id_booking))
        assert res.status_code == 404
        assert schema.validate(res.json()) == create_booking.get('booking')
