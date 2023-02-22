from django.db import models
import mysql.connector


#Creating connection object
#mydb=mysql.connector(
   # host="localhost",
  #  user="yourusername",
 #   password ="you_pasword")
#print(mydb)
class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self) -> str:
        return self.lastname

    class Meta:
        managed = False
        db_table = 'agentname'
        verbose_name_plural = "Agent Names"



class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.lga_name)

    class Meta:
        managed = False
        db_table = 'announced_lga_results'
        verbose_name_plural = "Announced LGA Results"


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.party_abbreviation

    class Meta:
        managed = False
        db_table = 'announced_pu_results'
        verbose_name_plural = "Announced Pu Results"



class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.state_name

    class Meta:
        managed = False
        db_table = 'announced_state_results'
        verbose_name_plural = "Announced State Results"



class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.ward_name

    class Meta:
        managed = False
        db_table = 'announced_ward_results'
        verbose_name_plural = "Announced Ward Results"


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField(auto_now=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.lga_name

    class Meta:
        managed = False
        db_table = 'lga'
        verbose_name_plural = "Local Govt Areas"



class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.partyname

    class Meta:
        managed = False
        db_table = 'party'
        verbose_name_plural = 'Political Parties'
        


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.polling_unit_id)
    class Meta:
        managed = False
        db_table = 'polling_unit'
        verbose_name_plural = "Polling Units"



class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.state_name

    class Meta:
        managed = False
        db_table = 'states'
        verbose_name_plural = "States"



class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.ward_name

    class Meta:
        managed = False
        db_table = 'ward'
        verbose_name_plural = "Wards"

# Create your models here.
