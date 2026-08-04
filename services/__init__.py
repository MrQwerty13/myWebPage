from services.auth_service import AuthService, AuthError
from services.post_service import PostService, PostError
from services.like_service import LikeService
from services.comment_service import CommentService, CommentError

auth_service = AuthService()
post_service = PostService()
like_service = LikeService()
comment_service = CommentService()

__all__ = [
    "auth_service",
    "post_service",
    "like_service",
    "comment_service",
    "AuthError",
    "PostError",
    "CommentError",
]
