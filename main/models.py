from django.db import models

from utils import NULLABLE
from users.models import User


# class Match(models.Model):
#     user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_user1')
#     user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_user2')
#
#     def __str__(self):
#         return f'Match between {self.user1} and {self.user2}'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    liked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_received')
    created_at = models.DateTimeField(auto_now_add=True)

