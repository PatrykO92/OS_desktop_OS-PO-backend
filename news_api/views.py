import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


class NewsAPIEndpoint(APIView):
    def get(self, request):
        # Define default values for optional query parameters
        country = "us"
        category = None
        page_size = 5 # Default page size

        # Override default values with query parameters if they are present
        if 'country' in request.query_params:
            country = request.query_params['country']
        if 'category' in request.query_params:
            category = request.query_params['category']
  
        

        # Make the request to NewsAPI with the optional parameters
        url = "https://newsapi.org/v2/top-headlines"
        params = {"country": country, "apiKey": NEWS_API_KEY, "pageSize": page_size}
        if category:
            params["category"] = category

        response = requests.get(url, params=params)

        # Return the response from NewsAPI
        return Response(response.json())
