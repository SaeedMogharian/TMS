# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class UserType(models.TextChoices):
        EMPLOYER = "E", "صاحب کار"
        CONTRACTOR = "C", "جویای کار"

    type = models.CharField(
        max_length=1,
        default=UserType.CONTRACTOR,
        choices=UserType.choices,
    )

    def __str__(self):
        return str(self.user) + ' | ' + str(self.type)


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = "P", "تعریف شده"
        ASSIGNED = "A", "واگذار شده"
        DONE = "D", "انجام شده"

    title = models.CharField(max_length=60)
    value = models.PositiveIntegerField()
    time = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='owner')
    description = models.TextField(blank=True)

    state = models.CharField(
        max_length=1,
        default=TaskStatus.PENDING,
        choices=TaskStatus.choices,
    )

    created_at = models.DateField(auto_now_add=True)

    assigned_contractor = models.ForeignKey(
        UserDetail,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contractor'
    )

    @property
    def is_assigned(self) -> bool:
        return self.assigned_contractor is not None

    def __str__(self):
        return self.title

    # @classmethod
    # def get_all_data_to_show(cls) -> List:
    #     """return tasks data for previewing"""
    #     result = []
    #     tasks = list(cls.objects.all().order_by("-created_at").values())
    #
    #     for task in tasks:
    #         owner = str(User.objects.get(pk=task.get("owner_id")))
    #         state = Task.objects.get(id=task.get("id")).get_state_display()
    #         task["owner"] = owner
    #         task["state"] = state
    #         result.append(task)
    #     return result

    # def assign_contractor(self, contractor: User) -> None:
    #     self.assigned_contractor = contractor
    #     self.state = Task.TaskStatus.ASSIGNED
    #     self.save()

    def done(self) -> None:
        self.state = Task.TaskStatus.DONE
        self.save()
