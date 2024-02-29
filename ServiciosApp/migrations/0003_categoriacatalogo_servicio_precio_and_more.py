# Generated by Django 4.0.5 on 2024-02-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0002_alter_servicio_contenido_alter_servicio_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCatalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.AddField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='categorias',
            field=models.ManyToManyField(to='ServiciosApp.categoriacatalogo'),
        ),
    ]
