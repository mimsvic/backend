# Generated by Django 5.1.5 on 2025-03-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_disciplina'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='carga_horaria',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.CharField(default='back-end', max_length=50),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='semestre',
            field=models.CharField(default='2º Semestre', max_length=20),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='sigla',
            field=models.CharField(max_length=20),
        ),
    ]
