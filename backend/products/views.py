from django.http import JsonResponse
import joblib
import os
import pandas as pd

# Paths to model files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml-model/recommendation_model.joblib")
DATA_PATH = os.path.join(BASE_DIR, "ml-model/user_product_interactions.csv")

# Load model and data
recommendation_model = joblib.load(MODEL_PATH)
data_frame = pd.read_csv(DATA_PATH)

def recommend_products(request):
    # Fetch the user_id from request
    user_id = request.GET.get('user_id')
    if not user_id:
        return JsonResponse({"error": "User ID is required"}, status=400)
    
    # Example logic for recommendations
    # Assuming `recommendation_model` uses user_id as input and outputs product IDs
    # Replace the following line with the actual logic for generating recommendations
    recommendations = recommendation_model.predict([int(user_id)])[:5]
    
    # Match product IDs to their names (if your CSV has product_id and product_name columns)
    product_ids = recommendations
    product_names = data_frame[data_frame['product_id'].isin(product_ids)]['product_name'].tolist()

    # Prepare the response
    response_data = [
        {"product_id": pid, "name": pname}
        for pid, pname in zip(product_ids, product_names)
    ]
    return JsonResponse({"user_id": user_id, "recommendations": response_data})
