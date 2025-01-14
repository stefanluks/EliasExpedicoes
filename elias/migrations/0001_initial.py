# Generated by Django 4.2 on 2023-08-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atrativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do atrativo')),
            ],
        ),
        migrations.CreateModel(
            name='AtrativoDia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField(default=1, verbose_name='Dia do Pacote')),
                ('atrativos', models.ManyToManyField(blank=True, to='elias.atrativo')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da Experiência')),
                ('atrativos', models.ManyToManyField(blank=True, to='elias.atrativo')),
            ],
        ),
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do Pacote')),
                ('descricao', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Descrição do pacote')),
                ('valor', models.FloatField(default=0, verbose_name='Valor do pacote (por pessoa)')),
                ('limite', models.IntegerField(default=4, verbose_name='Minímo de turistas')),
                ('saida', models.DateField(blank=True, null=True, verbose_name='Data de Saida')),
                ('volta', models.DateField(blank=True, null=True, verbose_name='Data da volta')),
                ('capa', models.FileField(blank=True, null=True, upload_to='static/imagens/', verbose_name='Imagem de Capa')),
                ('atrativo_dias', models.ManyToManyField(blank=True, to='elias.atrativodia')),
                ('experiencias', models.ManyToManyField(blank=True, to='elias.experiencia')),
            ],
        ),
    ]
