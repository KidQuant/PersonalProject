from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum
from xmlrpc.client import boolean


router = APIRouter(
    prefix='/blog',
    tags = ['blog']
)


# @router.get('/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@router.get(
    '/all',
    summary= 'Retrive all blogs',   #Provides the summary in the header API
    description= 'This api simulates fetching all blogs.',  #More description details
    response_description= 'List of available blogs' #description of what should hrouteren with a successful resposne
    )
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message' : f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: boolean = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'Blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog Type {type}'}


@router.get('/{id}', status_code= status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'Blog with id {id}' }


