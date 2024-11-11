from django import forms
from .models import AddCourse

class AddCourseForm(forms.MOdelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

from django import forms
from .models import Marks
