# Generated by Django 2.2.3 on 2019-08-07 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Alumini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=50)),
                ('thought', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BestPratices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('club_details', models.TextField()),
                ('club_photo', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('date', models.DateTimeField(blank=True)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('pdf_file', models.FileField(default=None, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('phone_num', models.CharField(max_length=10)),
                ('thought', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('companys', models.ManyToManyField(to='skctapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('dep_image', models.ImageField(null=True, upload_to='image')),
                ('video', models.URLField(null=True)),
                ('about', models.TextField(null=True)),
                ('vision', models.TextField(null=True)),
                ('mission', models.TextField(null=True)),
                ('academics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skctapp.Academics')),
                ('bp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skctapp.BestPratices')),
                ('club', models.ManyToManyField(to='skctapp.Club')),
                ('events', models.ManyToManyField(to='skctapp.Events')),
                ('facultys', models.ManyToManyField(to='skctapp.Faculty')),
                ('gallery', models.ManyToManyField(to='skctapp.Images')),
                ('hod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skctapp.Hod')),
                ('labs', models.ManyToManyField(to='skctapp.Lab')),
                ('placement', models.ManyToManyField(to='skctapp.Placement')),
                ('researches', models.ManyToManyField(to='skctapp.Pdf')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='students',
            field=models.ManyToManyField(to='skctapp.Student'),
        ),
    ]
