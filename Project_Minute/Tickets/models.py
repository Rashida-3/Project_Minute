from django.db import models


# Create your models here.

class State_Master(models.Model):
    # id=models.AutoField(primary_key=True,auto_created=True)
    state_name=models.CharField(200)
    state_code=models.CharField(200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_data=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True) 

    def __str__(self):
        return self.state_name

class User_Master(models.Model):
    Name=models.CharField(200)
    email=models.EmailField()
    password=models.CharField(20)
    phone=models.IntegerField()
    city=models.CharField(200)
    gender=models.CharField()
    joining_data=models.DateTimeField()
    state=models.ForeignKey(State_Master, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_data=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


class Task_Master(models.Model):
    task_id=models.CharField(200)
    title=models.CharField(200)
    description=models.TextField()
    assign_date=models.DateTimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    state=models.ForeignKey(State_Master, on_delete=models.CASCADE)
    updated_data=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User_Master, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

  