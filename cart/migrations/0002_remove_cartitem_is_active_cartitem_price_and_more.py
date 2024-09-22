from django.db import migrations, models
from decimal import Decimal

class Migration(migrations.Migration):
    dependencies = [
        ('cart', '0001_initial'),  # Adjust to your actual migration dependency
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=10, decimal_places=2),
        ),
    ]
