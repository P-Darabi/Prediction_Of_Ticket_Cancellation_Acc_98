😊🎉 Prediction of Ticket Cancellation with XGBoost Classifier 😊🎉

Introduction to the Problem:
The objective of this exercise is to develop a model that accurately predicts whether users will cancel their tickets. Each cancellation incurs a fine for the ticket registration site from the passenger company. Therefore, it is crucial to identify tickets that are likely to be canceled, enabling effective risk management within the company. By utilizing the available data, we will train a model to accurately detect trip cancellations.

Introduction to the Dataset:
The dataset comprises diverse information about passengers who have registered for a trip through a travel booking website. Below is a description of the columns present in the dataset:

    Created: The timestamp indicating the time of ticket registration.
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

This dataset provides valuable insights into passenger travel patterns, booking behavior, and trip cancellations. It can be utilized for various analyses and predictions within the travel industry.
