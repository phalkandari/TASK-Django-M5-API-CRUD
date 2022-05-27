# Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M5-API-CRUD).
2. Create a `virtual environment`.
3. Install the packages using `pip install -r dev-requirements.txt`.
4. Create an API detail view:
   - Which will display the following fields for the `Booking` object:
     - `id`
     - `flight`
     - `date`
     - `passengers`
   - Create a `URL` with name `booking-details` for this view and test it in `postman`.
5. Create an API update view:
   - which will allow you to edit the following fields for the `Booking` object:
     - `passengers`
     - `date`
   - Create a `URL` with name `update-booking` for this view and test it in `postman`.
6. Create an API delete view to cancel a `Booking`.
   - Create a `URL` with name `cancel-booking` for this view and test it in `postman`.
7. Push your code
