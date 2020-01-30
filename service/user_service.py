from database.models import User
from dto.user_dto import UserDto


def get_user_by_name(name):
    users = User.objects.filter(name=name)

    usersDto = []
    for u in users:
        usersDto.append(u.to_dto())
    return usersDto
