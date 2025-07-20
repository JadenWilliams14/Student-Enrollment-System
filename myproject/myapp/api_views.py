from rest_framework import viewsets, permissions
from .models import Student  # Import your model(s)
from .serializers import StudentSerializer  # Import your serializer(s)
from .permissions import IsOwnerOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows YourModel objects to be viewed or edited.
    Provides list, create, retrieve, update, partial_update, destroy actions.
    """
    queryset = Student.objects.all().order_by(
        'student')  # Or appropriate ordering
    serializer_class = StudentSerializer

    # Read operations allowed if IsAuthenticated passes.
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    # Filtering configuration (uses global DEFAULT_FILTER_BACKENDS)
    # Fields for exact matches (e.g., ?field1=value)
    filterset_fields = ['name', 'student']
    # Fields for ?search=... parameter
    search_fields = ['name', 'major']
    # Fields allowed for ?ordering=...
    ordering_fields = ['student', 'enrollment_date']

    # Optional: Implement custom logic, e.g., setting owner on create
    def perform_create(self, serializer):
        # Assumes 'owner' field exists on YourModel and is linked to User
        serializer.save(owner=self.request.user)
