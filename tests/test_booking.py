from model.booking import BookingData


class TestBooking:

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

    def test_create_new_booking(self, client):
        """
            1. Add new booking
            2. Check data and status
            3. Validate schema
        """

        client.booking.create_booking(data)
        # data = BookingData().random()
        # res = client.create_booking(data)
        # assert res.status_code == 200
        # booking_info = res.json()
        # assert booking_info.get('booking') == data
