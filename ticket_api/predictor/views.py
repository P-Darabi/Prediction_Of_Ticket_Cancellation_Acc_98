from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import xgboost as xgb
import os

# بارگذاری مدل XGBoost ذخیره شده به صورت JSON
model_path = './xgb_ticket.json'
model = xgb.Booster()
model.load_model(model_path)

class PredictCancellation(APIView):
    def post(self, request):
        data = request.data
        try:
            df = pd.DataFrame([data])
            dmatrix = xgb.DMatrix(df)
            prediction = model.predict(dmatrix)
            return Response({
                "cancellation_probability": round(float(prediction[0]), 3),
                "cancellation_prediction": int(prediction[0] > 0.5)
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

