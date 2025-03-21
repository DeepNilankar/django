from django.db import models



from django.db import models

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.start_time)

class TimeSlotRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
