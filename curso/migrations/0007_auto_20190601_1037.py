# Generated by Django 2.2.1 on 2019-06-01 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_auto_20190530_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHasMatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=1, max_digits=2)),
                ('matter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curso.Matter')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curso.Student')),
            ],
        ),
        migrations.AddField(
            model_name='matter',
            name='students',
            field=models.ManyToManyField(through='curso.StudentHasMatter', to='curso.Student'),
        ),
    ]
