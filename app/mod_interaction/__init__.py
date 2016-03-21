# coding=utf-8
__author__ = 'smallfly'

# 存放了用户数据, 以及活动之类的互动.

from flask import Blueprint
interaction_blueprint = Blueprint("interaction", __name__, url_prefix="/interaction")   # url 必须以 / 开头

# 加载数据表
from app.mod_interaction import models

# 加载Resource
from app.mod_interaction.resources import UserResource
from app.mod_interaction.resources import PostResource
from app.mod_interaction.resources import CommentResource
from app.mod_interaction.resources import ThumbUpResource
from app.mod_interaction.resources.GenericResource import GenericResource

from flask_restful import Api

api = Api(interaction_blueprint, prefix="/api/v2")

# curl localhost:8080/interaction/api/v2/user/1
# curl --header "Content-type: application/json" localhost:8080/interaction/api/v2/user -X PUT -d '{"id": 1, "birthday": "819648000", "nickname": "拂晓", "gender": 1, "profile": "hello world", "token": "000000", "uid": 1}'
# curl -i -X DELETE localhost:8080/interaction/api/v2/user/1
api.add_resource(GenericResource, "/user/<int:id>", "/user", endpoint="user", resource_class_kwargs=UserResource.INITIAL_KWARGS)

# curl localhost:8080/interaction/api/v2/post/1
# curl localhost:8080/interaction/api/v2/post -i --header "Content-type: application/json" -X POST -d '{"title": "testing_title", "content": "haha", "description": "click me", "uid": 1, "post_type": 1}'
# curl localhost:8080/interaction/api/v2/post -i --header "Content-type: application/json" -X PUT -d '{"title": "testing_title", "content": "haha", "id": 2, "description": "do not click me", "uid": 1, "post_type": 1}'
# api.add_resource(PostResource, "/post/<int:id>", "/post", endpoint="post")
api.add_resource(GenericResource, "/post/<int:id>", "/post", endpoint="post", resource_class_kwargs=PostResource.INITIAL_KWARGS)

# curl localhost:8080/interaction/api/v2/comment/1
# curl localhost:8080/interaction/api/v2/comment -i -X POST -H "Content-type:application/json" -d '{"token": "000000", "post_id": 1, "uid": 1, "comment": "nice post!"}'
# curl localhost:8080/interaction/api/v2/comment -i -X PUT -H "Content-type:application/json" -d '{"token": "000000", "id": 1, "post_id": 1, "uid": 1, "comment": "amazing post!"}'
# curl -i -X DELETE localhost:8080/interaction/api/v2/comment --header "Content-type:application/json" -d '{ "uid": 1, "token": "00000", "id":1}'
api.add_resource(GenericResource, "/comment/<int:id>", "/comment", endpoint="comment", resource_class_kwargs=CommentResource.INITIAL_KWARGS)

# curl localhost:8080/interaction/api/v2/like/1
# curl localhost:8080/interaction/api/v2/like -i -X POST -H "Content-type:application/json" -d '{"post_id": 1, "uid": 1, "token": "000000"}'
# curl -i -X DELETE localhost:8080/interaction/api/v2/like/1 -H "Content-type:application/json" -d '{"uid": 1, "token": "000000", "id": 1}'
api.add_resource(GenericResource, "/like/<int:id>", "/like", endpoint="like", resource_class_kwargs=ThumbUpResource.INITIAL_KWARGS)





