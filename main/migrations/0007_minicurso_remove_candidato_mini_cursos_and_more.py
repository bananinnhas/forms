# Generated by Django 4.1.3 on 2022-11-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_candidato_email_candidato_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='mini_cursos',
        ),
        migrations.AddField(
            model_name='candidato',
            name='minicursos',
            field=models.ManyToManyField(to='main.minicurso'),
        ),
    ]
