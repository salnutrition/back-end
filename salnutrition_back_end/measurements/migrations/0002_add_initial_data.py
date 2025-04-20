from django.db import migrations, models

def create_initial_data(apps, schema_editor):
    # Get the model from the historical version
    MeasurementType = apps.get_model('measurements', 'MeasurementType')

    # Create initial data
    initial_data = [
        {'name': 'Weight', 'unit': 'kg'},
        {'name': 'Height', 'unit': 'cm'},
        {'name': 'BicepRight', 'unit': 'cm'},
        {'name': 'BicepLeft', 'unit': 'cm'},
        {'name': 'Chest', 'unit': 'cm'},
        {'name': 'Waist', 'unit': 'cm'},
        {'name': 'Hip', 'unit': 'cm'},
        {'name': 'ThighRight', 'unit': 'cm'},
        {'name': 'ThighLeft', 'unit': 'cm'},
        {'name': 'CalfRight', 'unit': 'cm'},
        {'name': 'CalfLeft', 'unit': 'cm'},
        {'name': 'ShoulderWidth', 'unit': 'cm'},
        {'name': 'Neck', 'unit': 'cm'},
        {'name': 'ForearmRight', 'unit': 'cm'},
        {'name': 'ForearmLeft', 'unit': 'cm'},
        {'name': 'WristRight', 'unit': 'cm'},
        {'name': 'WristLeft', 'unit': 'cm'},
        {'name': 'BodyFatPercentage', 'unit': '%'},
        {'name': 'MuscleMass', 'unit': 'kg'},
        {'name': 'BasalMetabolicRate', 'unit': 'kcal/day'},
        {'name': 'BodyMassIndex', 'unit': 'kg/m²'},
    ]

    # Bulk create the initial data
    MeasurementType.objects.bulk_create([MeasurementType(**data) for data in initial_data])

class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]