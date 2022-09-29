from django.shortcuts import render
from .models import Employee,EmployeeFace,Notification,Subscriber,Profile
from django.http import HttpResponseRedirect
from qr_code.qrcode.utils import QRCodeOptions
import socket
import uuid
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
import pickle
from .models import Employee,EmployeeFace,Notification,Ipdetail,Subscriber,Camera
from .forms import EmployeeForm,EmployeefaceForm
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponse
from django.http.response import JsonResponse, HttpResponse
from securite.serializers import EmployeeFaceSerializer,IpdetailSerializer,SubscriberSerializer,NotificationSerializer,EmployeeSerializer,ProfileSerializer,CameraSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets
import json
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

def login_user(request):
    logout(request)
    context=RequestContext(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request,'securite/login.html',{'message001':'Invalid Username/Password'})

    return render(request,'securite/login.html')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')



#######################################################################################################
@login_required
def members(request):
    user_id = request.user
    id = user_id.id
    employees = Employee.objects.all().filter(user_id = id)
    employees = Employee.objects.all()
    employeeface = EmployeeFace.objects.all()
    print(employees)
    print(employeeface)
    return render(request, 'securite/members.html',{'employeeface': employeeface,'employees': employees})


def save_employee_form(request, form, template_name):
    data = dict()
    user_id = request.user
    id = user_id.id
    if request.method == 'POST':
        if form.is_valid():
            form1=form.save(commit=False)
            form1.user = request.user
            form.save()
            data['form_is_valid'] = True
            employees = Employee.objects.all().filter(user_id = id)
            #employeeface = EmployeeFace.objects.all().filter(emp_id='fgh')
            #employeeface = get_object_or_404(Employee,emp_id='fgh')

            #printclass ExampleView(APIView):(employeeface)
            data['html_employee_list'] = render_to_string('securite/includes/partial_employee_list.html', {
                'employees': employees
                # 'employeeface': employeeface
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(form)
    else:
        form = EmployeeForm()
    return save_employee_form(request, form, 'securite/includes/partial_employee_create.html')



def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'securite/includes/partial_employee_update.html')



def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    user_id = request.user
    id = user_id.id
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = Employee.objects.all().filter(user_id = id)
        # employeeface = EmployeeFace.objects.all()
        data['html_employee_list'] = render_to_string('securite/includes/partial_employee_list.html', {
            'employees': employees
        })

    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('securite/includes/partial_employee_delete.html', context, request=request)
    return JsonResponse(data)

def employeeface_create(request,pk):
    employeeface = get_object_or_404(Employee, pk=pk)
    print(employeeface)
    data = dict()
    if request.method == 'POST':
        form = EmployeefaceForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.emp_id = employeeface
            form.save()
            data['form_is_valid'] = True
            employeeface = EmployeeFace.objects.all()
            data['html_employee_list'] = render_to_string('securite/includes/partial_employee_list.html', {
                'employeeface': employeeface
            })
        else:
            data['form_is_valid'] = False
    else:
        form = EmployeefaceForm(instance=employeeface)
    #return save_employeeface_form(request, form, 'employee/includes/partial_employeeface_create.html',employeeface)
    context = {'form': form}
    data['html_form'] = render_to_string( 'securite/includes/partial_employeeface_create.html', context, request=request)
    return JsonResponse(data)

#################################################################################################################




def report(request):
    employees = Employee.objects.all()
    return render(request, 'securite/report.html',{'employees': employees})


@login_required(login_url='/login/')
def subscriber(request):
	context={}
	user_id=request.user
	id=user_id.id
	subscriber=Subscriber.objects.filter(user_id=id)
	context.update({'subscriber':subscriber})
	return render(request,'securite/subscriberdetail.html',context)


def subscriber_delete(request, pk):
    print("subscriber")
    subscriber = get_object_or_404(Subscriber, pk=pk)
    print(subscriber)
    data = dict()
    user_id = request.user
    id = user_id.id
    if request.method == 'POST':
        print("post page")
        subscriber.delete()
        data['form_is_valid'] = True
        subscriber = Subscriber.objects.all().filter(user_id = id)
        # employeeface = EmployeeFace.objects.all()
        data['html_notification_list'] = render_to_string('securite/includes/partial_subscriber_list.html', {
            'subscriber': subscriber
        })

    else:
        print("post page")
        subscriber.delete()
        data['form_is_valid'] = True
        subscriber = Subscriber.objects.all().filter(user_id = id)
        # employeeface = EmployeeFace.objects.all()
        data['html_notification_list'] = render_to_string('securite/includes/partial_subscriber_list.html', {
            'subscriber': subscriber
        })
    return JsonResponse(data)

def camera(request):
    pass
    return render(request, 'securite/camera.html')



def notifications(request):
    user_id = request.user
    id = user_id.id
    notifications = Notification.objects.all().filter(user_id = id)
    return render(request, 'securite/notifications.html', {'notifications': notifications})

def notification_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    print(pk)
    data = dict()
    user_id = request.user
    id = user_id.id
    if request.method == 'POST':
        print("post page")
        notification.delete()
        data['form_is_valid'] = True
        notifications = Notification.objects.all().filter(user_id = id)
        # employeeface = EmployeeFace.objects.all()
        data['html_notification_list'] = render_to_string('securite/includes/partial_notification_list.html', {
            'notifications': notifications
        })

    else:
        print("post page")
        notification.delete()
        data['form_is_valid'] = True
        notifications = Notification.objects.all().filter(user_id = id)
        # employeeface = EmployeeFace.objects.all()
        data['html_notification_list'] = render_to_string('securite/includes/partial_notification_list.html', {
            'notifications': notifications
        })
    return JsonResponse(data)




def intrusions(request):
    pass
    return render(request, 'securite/intrusions.html')


def network(request):
    user_id = request.user
    id = user_id.id
    if request.POST:
        wifiname = request.POST['wifiname']
        wifipassword = request.POST['wifipassword']
        print(wifiname)
        print(wifipassword)
        #return render(request, 'securite/network.html', context=context)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    MacAddr = uuid.getnode()
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    context = dict(
    my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )
    context.update({'ip':IPAddr, 'mac':MacAddr })
    return render(request, 'securite/network.html', context=context)

def door(request):
    user_id = request.user
    id = user_id.id
    if request.POST:
        wifiname = request.POST['wifiname']
        wifipassword = request.POST['wifipassword']
        print(wifiname)
        print(wifipassword)
        #return render(request, 'securite/network.html', context=context)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    MacAddr = uuid.getnode()
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    context = dict(
    my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)
    context.update({'ip':IPAddr, 'mac':MacAddr })
    return render(request, 'securite/door.html', context=context)

def calendar(request):
    user_id = request.user
    id = user_id.id
    notifications = Notification.objects.all().filter(user_id = id)
    return render(request, 'securite/calendar.html',{'notifications': notifications})

#fields = ('fullname','location','birth_date','gender','phone','image','user')
def profile(request):
    user=request.user
    id=user.id
    context = {}
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        location = request.POST.get('location')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        print(image)
        obj = Profile.objects.all().delete()
        proObj = Profile.objects.create(user_id=id,fullname=fullname,location=location,birth_date=birth_date,gender=gender,phone=phone,email=email,image=image)
        proObj.save()
        message = 'camera Added Successfully'
        return render(request, 'securite/profile.html', context)
    return render(request, 'securite/profile.html', context)

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'securite/profile.html'


class ProfileView(CreateView):
	fields = ('fullname','location','birth_date','gender','phone','image','email')
	model = Profile
	template_name = 'registration.html'

	def dispatch(self, *args, **kwargs):
		return super(ProfileView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return redirect('/')

class ProfileUpdateView(UpdateView):
	fields = ('fullname','location','birth_date','gender','phone','image','email')
	model = Profile
	template_name = 'registration.html'

	def dispatch(self, *args, **kwargs):
		return super(ProfileUpdateView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return redirect('/')


# class ProfileView1(CreateView):
# 	fields = ('fullname','location','birth_date','gender','phone','image','user')
# 	model = models.Profile
# 	template_name = 'registration1.html'

def member_detail(request,pk):
    detail=Employee.objects.get(id=pk)
    return render(request, 'securite/member_detail.html',{'detail':detail})



################################################################################

class FaceAPI(APIView):
	parser_classes = (MultiPartParser, FormParser)
	permission_classes = (IsAuthenticated,)
	def post(self, request, *args, **kwargs):
		print(request.user.id)
		users = EmployeeFace.objects.filter(emp_id=request.user.id)
		file_serializer = EmployeeFaceSerializer(data=request.data)
		if file_serializer.is_valid():
			file=file_serializer.save()
			file.user =self.request.user
			file.save()
			#users = Facedetail.objects.filter(user_id=request.user.id)
			#file_serializer = FacedetailSerializer(users,many=False)
			print(file_serializer.data)
			return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, *args, **kwargs):
		users = EmployeeFace.objects.filter(emp_id=request.user.id)
		file_serializer = EmployeeFaceSerializer(users, many=True)
		print(json.dumps(file_serializer.data))
		print(request.user,request.auth)
		return JsonResponse(file_serializer.data, safe=False)


class IpAPI(APIView):
	parser_classes = (MultiPartParser, FormParser)
	permission_classes = (IsAuthenticated,)
	def post(self, request, *args, **kwargs):
		print(request.user.id)
		users = Ipdetail.objects.filter(user_name=request.user.id)
		file_serializer = IpdetailSerializer(data=request.data)
		if file_serializer.is_valid():
			file=file_serializer.save()
			file.user =self.request.user
			file.save()
			print(file_serializer.data)
			return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, *args, **kwargs):
		users = Ipdetail.objects.filter(user_name=request.user.id)
		file_serializer = IpdetailSerializer(users, many=True)
		print(json.dumps(file_serializer.data))
		print(request.user,request.auth)
		return JsonResponse(file_serializer.data, safe=False)

@api_view(['GET','POST'])
def SubscriberAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        subscribers = Subscriber.objects.filter(user_id=id)
        print(subscribers)
        serializer = SubscriberSerializer(subscribers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        print(data)
        serializer = SubscriberSerializer(data=data)
        if serializer.is_valid():
            print(2)
            file=serializer.save()
            file.user = request.user
            file.save()
            subscribers = Subscriber.objects.filter(user_id=id)
            serializer = SubscriberSerializer(subscribers, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=500)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def NotificationAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        notifications = Notification.objects.filter(user_id=id)
        serializer = NotificationSerializer(notifications, many=True)
        return JsonResponse(serializer.data[::-1], safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            notifications = Notification.objects.filter(user_id=id)
            serializer = NotificationSerializer(notifications, many=True)
            return JsonResponse(serializer.data[::-1], safe=False)
        return JsonResponse(serializer.errors, status=500)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def EmployeeAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        notifications = Employee.objects.filter(user_id=id)
        serializer = EmployeeSerializer(notifications, many=True)
        return JsonResponse(serializer.data[::-1], safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            notifications = Employee.objects.filter(user_id=id)
            serializer = EmployeeSerializer(notifications, many=True)
            return JsonResponse(serializer.data[::-1], safe=False)
        return JsonResponse(serializer.errors, status=500)


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def ProfileAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        notifications = Profile.objects.filter(user_id=id)
        serializer = ProfileSerializer(notifications, many=True)
        return JsonResponse(serializer.data[::-1], safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            notifications = Profile.objects.filter(user_id=id)
            serializer = ProfileSerializer(notifications, many=True)
            return JsonResponse(serializer.data[::-1], safe=False)
        return JsonResponse(serializer.errors, status=500)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def CameraAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        notifications = Camera.objects.filter(user_id=id)
        serializer = CameraSerializer(notifications, many=True)
        return JsonResponse(serializer.data[::-1], safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = CameraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            notifications = Camera.objects.filter(user_id=id)
            serializer = CameraSerializer(notifications, many=True)
            return JsonResponse(serializer.data[::-1], safe=False)
        return JsonResponse(serializer.errors, status=500)


################################################################################
