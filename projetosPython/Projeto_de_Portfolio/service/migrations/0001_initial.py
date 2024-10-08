# Generated by Django 4.2.9 on 2024-02-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(max_length=15)),
                ('servico', models.CharField(choices=[('portfolio', 'Portfólio'), ('blog', 'Blog'), ('site', 'Site')], max_length=10)),
            ],
        ),
    ]
