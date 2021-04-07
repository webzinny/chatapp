from django.db import models

#-------------------------------------------USER TABLE-------------------------------------------------
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    phone_no = models.IntegerField()

    def __str__(self):
        return (self.email)

#-------------------------------------------Friend TABLE-------------------------------------------------
class Friend(models.Model):
    user1_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user1')
    user2_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user2')
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(models.Model):
        return str(self.id)

#------------------------------------------friend's message TABLE------------------------------------------
class friend_message(models.Model):
    friend_id = models.ForeignKey(Friend,on_delete=models.CASCADE)
    sender_id = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    message = models.TextField()

#------------------------------------------------Group TABLE------------------------------------------------
class Group(models.Model):
    creater_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user id')
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)

#-------------------------------------------Participants TABLE-------------------------------------------------
class Participants(models.Model):
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='group id')
    participant_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user id')

#-------------------------------------------Group message TABLE-------------------------------------------------
class group_message(models.Model):
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='group id')
    sender_id = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
