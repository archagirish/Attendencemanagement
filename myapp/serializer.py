from rest_framework.serializers import ModelSerializer, ImageField 
from rest_framework import serializers
from myapp.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = StudentTable
        fields = ['name', 'email', 'phonenumber', 'image']

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification_model
        fields = ['notification', 'date']

class SendComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['complaint']
class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['complaint', 'reply']

class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password']


from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentTable
        fields = ['id', 'department']  # Include relevant fields like id and name


class TimetableSerializer(serializers.ModelSerializer):
    subject1 = serializers.CharField(source='slot_9_10.Subject')
    subject2 = serializers.CharField(source='slot_10_11.Subject')
    subject3 = serializers.CharField(source='slot_11_12.Subject')
    subject4 = serializers.CharField(source='slot_1_2.Subject')
    subject5 = serializers.CharField(source='slot_2_3.Subject')
    subject6 = serializers.CharField(source='slot_3_4.Subject')
    class Meta:
        model = Timetable1
        fields = ['day', 'subject1','subject2', 'subject3', 'subject4', 'subject5', 'subject6']  # Include relevant fields like id and name

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceTable
        fields = ['Date', 'Attendance', 'Period']  # Include relevant fields like id and name