from django.db import models
from django.db.models.signals import post_save

class Employee(models.Model):
    em_create_date = models.DateField('Ngày tạo')
    em_code = models.CharField(max_length=50, unique=True)
    em_name = models.CharField(max_length=200)
    status = models.SmallIntegerField(max_length=2)

    def __str__(self):
        return self.em_name

class GiaoDich(models.Model):
    em = models.ForeignKey(Employee, on_delete=models.CASCADE)
    create_date = models.DateField('Ngày tạo')
    status = models.SmallIntegerField(max_length=2)
    from_serial = models.BigIntegerField()
    to_serial = models.BigIntegerField()

    def __str__(self):
        return self.id

class GiaoDichDetail(models.Model):
    gd = models.ForeignKey(GiaoDich, on_delete=models.CASCADE)
    em = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.SmallIntegerField(max_length=2)
    create_date = models.DateField('date created')
    serial = models.BigIntegerField()
    note = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.serial

def create_gd_detail(sender, **kwargs):
    if kwargs['created']:
        giao_dich = kwargs.get('instance')
        for serial in range(giao_dich.from_serial, giao_dich.to_serial+1):
            try:
                gd_detail = GiaoDichDetail()
                gd_detail.em = giao_dich.em
                gd_detail.gd = giao_dich
                gd_detail.serial = serial
                gd_detail.create_date = giao_dich.create_date
                gd_detail.status = 1
                gd_detail.save()
            except Exception as e:
                print(e)

post_save.connect(create_gd_detail, sender=GiaoDich)
