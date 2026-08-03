from services.auth_service import AuthService, AuthError
from services.post_service import PostService, PostError
from services.like_service import LikeService

auth_service = AuthService()
post_service = PostService()
like_service = LikeService()

__all__ = [
    "auth_service",
    "post_service",
    "like_service",
    "AuthError",
    "PostError",
]
