from django.db import models
import uuid # for unique key


class User(models.Model):
    """Model recording user credentials."""
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique User ID', editable=False)
    name = models.CharField(max_length=50, help_text='Legal Name')
    hashedpw = models.CharField(max_length=200, help_text='Hashed Password')
    school_id = models.ForeignKey(School, on_delete=models.SET(0))
    points = models.PositiveIntegerField(default=0, help_text='Points possessed', blank=True)
    
    # Metadata
    class Meta: 
    ordering = ['-id']

    # Methods
    def __str__(self):
        return self.name

class School(models.Model):
    """Model recording school details."""
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique School ID')
    name = models.CharField(max_length=50, help_text='School Name')
    
    # Metadata
    class Meta: 
    ordering = ['-id']

    # Methods
    def __str__(self):
        return self.name

class Course(models.Model):
    """Model recording course details."""
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Course ID')
    name = models.CharField(max_length=50, help_text='Course Name')
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
    ordering = ['-id']

    # Methods
    def __str__(self):
        return self.name

class Enroll(models.Model):
    """Model highlighting the courses a student takes."""
    
    # Fields
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
    ordering = ['-user_id']

    # Methods
    def __str__(self):
        return self.user_id + ":" + self.course_id

class File(models.Model):
    """Model managing file details."""
    
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique File ID', editable=False)
    name = models.CharField(max_length=200, help_text='File Name')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cost_point = models.PositiveIntegerField(default=1, help_text='Points cost to view the file', blank=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, help_text='Uploader (Student) ID')
    publish_date = models.DateField(help_text='Time Uploaded')

    # Metadata
    class Meta: 
    ordering = ['-publish_date']

    # Methods
    def __str__(self):
        return self.name

class Purchase(models.Model):
    """Model recording file purchase history of user."""
    
    # Fields
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
    ordering = ['-user_id']

    # Methods
    def __str__(self):
        return self.user_id + ":" + self.file_id