from django.db import models

class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()

class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.URLField(null=True)

    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.color + " " + self.manufacturer + " " + self.model_name

    class Meta:
        ordering = ("manufacturer",)
