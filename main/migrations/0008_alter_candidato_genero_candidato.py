# Generated by Django 4.1.3 on 2022-11-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_minicurso_remove_candidato_mini_cursos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='genero_candidato',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=50, verbose_name='Sexo: '),
        ),
    ]
