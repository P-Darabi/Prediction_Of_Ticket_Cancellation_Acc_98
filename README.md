# Prediction_Of_Ticket_Cancellation_Acc_98
Prediction Of Ticket Cancellation by XGBoost Classifier

Introduction Of Problem:
In this exercise, our goal is to predict whether users will cancel their tickets or not. Each cancellation imposes a fine on the ticket registration site from the passenger company. Therefore, identifying tickets that are likely to be canceled is crucial for effective risk management within the company. Using the available data, we will train a model to accurately detect trip cancellations.

Introduction Of Dataset:
The dataset contains various information about passengers who have registered for a trip through a travel booking website. Here is a description of the columns in the dataset:

Created: The timestamp indicates the ticket registration time.
CancelTime: The timestamp when the passenger canceled the ticket, if applicable.
DepartureTime: The scheduled departure time for the trip.
BillID: The unique identifier for the purchase transaction.
TicketID: The unique identifier for the ticket.
ReserveStatus: The payment status of the customer.
UserID: The unique identifier for the user.
Male: Indicates whether the ticket belongs to a male passenger or not.
Price: The ticket price without any discounts.
CouponDiscount: The discount applied by the passenger on the ticket.
From: The origin of the trip.
To: The destination of the trip.
Domestic: Indicates whether the trip is domestic or international.
VehicleType: Specifies details about the mode of transportation.
VehicleClass: Indicates whether the vehicle is first class or not.
Vehicle: Specifies the type of vehicle.
Cancel: Indicates whether the ticket has been canceled or not.
HashPassportNumber_p: Hashed version of the passport number.
HashEmail: Hashed version of the email address.
BuyerMobile: Hashed version of the buyer's mobile number.
NationalCode: Hashed version of the national identification number.
TripReason: The reason for the trip.

This dataset provides valuable insights into passenger travel patterns, booking behavior, and trip cancellations, which can be used for various analyses and predictions in the travel industry.

