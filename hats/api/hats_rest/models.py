from django.db import models

class LocationVO(models.Model):
    closet_name = models.CharField(max_length=100)
    import_href= models.CharField(max_length=200, unique=True)


class Hat(models.Model):
    fabric = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.URLField(max_length=1000, null=True )

    location = models.ForeignKey(
        LocationVO,
        related_name = "hats",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.color} {self.fabric} {self.style}"

    class Meta:
        ordering = ("style", "color", "fabric")
