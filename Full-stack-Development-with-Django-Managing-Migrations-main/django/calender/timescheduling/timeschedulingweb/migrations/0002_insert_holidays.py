from django.db import migrations

def insert_holidays(apps, schema_editor):  
    TimeSlot = apps.get_model('timeschedulingweb', 'TimeSlot')  
    TimeSlot(start_time='2025-05-01T00:00:00',  
             end_time='2025-05-01T23:59:59',  
             description='Labour day').save()  
    TimeSlot(start_time='2025-04-14T00:00:00',  
             end_time='2025-04-14T23:59:59',  
             description='Independence day').save()  
    TimeSlot(start_time='2025-12-25T00:00:00',  
             end_time='2025-12-25T23:59:59',  
             description='Religion fest').save()  

class Migration(migrations.Migration):  

    depndencies = [  
        ('timeschedulingweb', '0001_initial'),  
    ]  

    operations = [  
        migrations.RunPython(insert_holidays)  
    ]