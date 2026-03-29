from django.db import models

class BillRecord(models.Model):
    customer_name = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=50, default='bill book')
    start_no = models.IntegerField()
    end_no = models.IntegerField()

    # FIXED (migration issue)
    added_by = models.CharField(max_length=50, default="Admin")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} ({self.start_no}-{self.end_no})"