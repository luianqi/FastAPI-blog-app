from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, oauth2
from blog.database import get_db
from blog.schemas import ShowResponse
from blog.views import blog

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)


@router.get("/", response_model=List[ShowResponse])
def all_blogs(db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)
              ):

    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)
                ):
    return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),
            current_user: schemas.User = Depends(oauth2.get_current_user)
            ):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)
           ):
    return blog.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=ShowResponse)
def detail(id: int, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)
           ):
    return blog.detail(id, db)
