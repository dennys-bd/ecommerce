# Generated by Django 3.2.2 on 2021-05-08 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('external_id', models.UUIDField()),
                ('title', models.CharField(max_length=255)),
                ('image', models.URLField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('score', models.FloatField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('external_id', 'client'), name='unique product by client'),
        ),
    ]
