from django.contrib import admin
from .models import Course
from .models import Matter
from .models import Student
from .models import Teacher
from .models import StudentHasMatter

# Register your models here.

admin.site.register(Course)
admin.site.register(Matter)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentHasMatter)
