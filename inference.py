# -*- coding: utf-8 -*-
"""inference.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ufHYUNAIPhlyJ9X9ERSLyU3ssJG6EXUf
"""

from hotel_booking_model import HotelBookingModel

model = HotelBookingModel()

test_input = {
    'no_of_adults': 2,
    'no_of_children': 1,
    'no_of_weekend_nights': 2,
    'no_of_week_nights': 3,
    'type_of_meal_plan': 'Half Board',
    'required_car_parking_space': 0,
    'room_type_reserved': 'C',
    'lead_time': 30,
    'arrival_year': 2025,
    'arrival_month': 7,
    'arrival_date': 15,
    'market_segment_type': 'Online',
    'repeated_guest': 0,
    'no_of_previous_cancellations': 0,
    'no_of_previous_bookings_not_canceled': 2,
    'avg_price_per_room': 120.50,
    'no_of_special_requests': 1
}

print('Cancellation Prediction:', model.predict(test_input))