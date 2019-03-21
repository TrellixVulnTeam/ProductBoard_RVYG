# Generated by Django 2.1.1 on 2019-03-16 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0006_auto_20190101_2105'),
        ('KanbanBoard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BoardTitle', models.CharField(max_length=120)),
                ('AccessList', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('BoardProductList', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Products.myProducts')),
            ],
        ),
        migrations.RemoveField(
            model_name='lists',
            name='listitem',
        ),
        migrations.AddField(
            model_name='card',
            name='listitem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KanbanBoard.lists'),
        ),
        migrations.AddField(
            model_name='lists',
            name='BoardLists',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KanbanBoard.Board'),
        ),
    ]