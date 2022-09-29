from rest_framework import serializers
from securite.models import EmployeeFace,Ipdetail,Subscriber,Notification,Employee,Profile,Camera

class EmployeeFaceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = EmployeeFace
        fields = '__all__'

class IpdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipdetail
        fields = ["id","user_name","ipname"]

#
# class proccesimageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(max_length=None,use_url=True)
#     class Meta:
#         model = Facedetail
#         fields = ['image']

class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscriber
		fields = [
			"id",
			"SubscriberID",
			"ReservedField"
			]
class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = [
			"id",
			"Category",
			"CameraName",
			"ImageURL",
			"Stream",
            "Time"
			]
class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = [
			"emp_id",
			"emp_name",
			"designation",
			"email",
			"phone",
            "salary",
            "gender",
			]

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = [
			"id",
			"fullname",
			"location",
			"birth_date",
			"phone",
            "gender",
            "email",
            "image",
			]
class CameraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Camera
		fields = [
			"id",
			"name",
			"user",
			"stream",
            ]
