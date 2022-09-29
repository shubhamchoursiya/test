# Generated by Django 2.2.4 on 2019-09-20 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=100, unique=True)),
                ('emp_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('gender', models.CharField(choices=[('MA', 'male'), ('FE', 'female')], default='MA', max_length=2)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubscriberID', models.CharField(max_length=500, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ReservedField', models.CharField(default=0, max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('MA', 'male'), ('FE', 'female')], default='MA', max_length=2)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='userpics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=64)),
                ('CameraName', models.CharField(max_length=64)),
                ('ImageURL', models.CharField(max_length=64)),
                ('Stream', models.CharField(max_length=128)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('res1', models.CharField(default=0, max_length=100)),
                ('res2', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ipdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipname', models.CharField(max_length=100)),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='securite/')),
                ('res1', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res2', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res3', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res4', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res5', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res6', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res7', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res8', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res9', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res10', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res12', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res13', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res14', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res15', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res16', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res17', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res18', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res19', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res20', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res21', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res22', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res23', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res24', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res25', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res26', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res27', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res28', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res29', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res30', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res31', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res32', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res33', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res34', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res35', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res36', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res37', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res38', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res39', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res40', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res41', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res42', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res43', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res44', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res45', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res46', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res47', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res48', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res49', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res50', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res51', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res52', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res53', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res54', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res55', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res56', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res57', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res58', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res59', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res60', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res61', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res62', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res63', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res64', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res65', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res66', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res67', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res68', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res69', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res70', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res71', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res72', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res73', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res74', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res75', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res76', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res77', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res78', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res79', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res80', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res81', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res82', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res83', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res84', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res85', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res86', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res87', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res88', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res89', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res90', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res91', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res92', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res93', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res94', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res95', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res96', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res97', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res98', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res99', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res100', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res101', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res102', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res103', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res104', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res105', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res106', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res107', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res108', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res109', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res110', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res111', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res112', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res113', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res114', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res115', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res116', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res117', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res118', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res119', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res120', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res121', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res122', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res123', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res124', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res125', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res126', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res127', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('res128', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securite.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=500, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('stream', models.CharField(default=0, max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
