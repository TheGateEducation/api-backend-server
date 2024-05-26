"""Views for the student app."""
from rest_framework import viewsets, permissions
from student.api.serializers import StudentRecordSerializer
from core.models import StudentRecord

class StudentRecordViewSet(viewsets.ModelViewSet):
    """Manage student records in the database."""
    serializer_class = StudentRecordSerializer
    queryset = StudentRecord.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve the student records for the authenticated user."""
        return self.queryset

    def perform_create(self, serializer):
        """Create a new student record."""
        serializer.save()