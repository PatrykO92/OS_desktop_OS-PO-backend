from rest_framework import generics, permissions
from .models import Score
from .serializers import ScoreSerializer

class HighScores(generics.ListCreateAPIView):
    
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Score.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)