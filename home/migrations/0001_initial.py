# Generated by Django 3.2.9 on 2022-11-11 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Usuario')),
                ('telefono', models.CharField(max_length=10, verbose_name='Télefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('tipo_usuario', models.CharField(max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Albumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('anio_publicacion', models.DateField()),
                ('num_canciones', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albumes',
            },
        ),
        migrations.CreateModel(
            name='Continentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Continente',
                'verbose_name_plural': 'Continentes',
            },
        ),
        migrations.CreateModel(
            name='Discos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edicion', models.CharField(max_length=30)),
                ('condicion', models.CharField(max_length=30)),
                ('id_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.albumes')),
            ],
            options={
                'verbose_name': 'Disco',
                'verbose_name_plural': 'Discos',
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apep', models.CharField(max_length=30, verbose_name='Apellido Paterno')),
                ('apem', models.CharField(max_length=30, verbose_name='Apellido Materno')),
                ('genero', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='usuarios_codigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_reg', models.CharField(max_length=10)),
                ('estatus_reg', models.IntegerField(null=True)),
                ('tipo_usuario', models.CharField(max_length=20, null=True)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personas')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=240)),
                ('id_disco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.discos')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('id_continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.continentes')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.AddField(
            model_name='discos',
            name='id_pais_fabricacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paises'),
        ),
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('duracion', models.IntegerField(null=True)),
                ('id_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.albumes')),
            ],
            options={
                'verbose_name': 'Cancion',
                'verbose_name_plural': 'Canciones',
            },
        ),
        migrations.CreateModel(
            name='Artistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paises')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
            },
        ),
        migrations.AddField(
            model_name='albumes',
            name='id_artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.artistas'),
        ),
        migrations.AddField(
            model_name='albumes',
            name='id_genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.generos'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personas', verbose_name='Persona'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
