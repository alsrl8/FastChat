from database import MongoClient
from database import User


async def find_user_by_google_email(google_email: str) -> User:
    user = await MongoClient.get_client().user.userinfo.find_one({
        'google_email': google_email
    })
    if not user:
        print('No User')
        return User()

    return user
