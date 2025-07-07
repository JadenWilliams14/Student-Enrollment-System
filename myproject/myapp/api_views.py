from rest_framework import viewsets, permissions
from .models import Student  # Import your model(s)
from .serializers import StudentSerializer  # Import your serializer(s)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows YourModel objects to be viewed or edited.
    Provides list, create, retrieve, update, partial_update, destroy actions.
    """
    queryset = Student.objects.all().order_by(
        '-student')  # Or appropriate ordering
    serializer_class = StudentSerializer

    # Optional: Override default permissions just for this viewset
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Optional: Implement custom logic, e.g., setting owner on create
    def perform_create(self, serializer):
        # Assumes 'owner' field exists on YourModel and is linked to User
        serializer.save(owner=self.request.user)
