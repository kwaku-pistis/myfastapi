from fastapi import FastAPI, Query, Path, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import  Optional, List, Set

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="The descripton of the item", max_length=300)
    price: float = Field(..., description="The price must be greater than 0", gt=0)
    tax: Optional[float] = None
    tags: List[str] = []
    unique_tags: Set[str] = set() # making the contents of the list unique []
    image: Optional[image] = None # a sub-model
    
    
class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    
    
class Image(BaseModel):
    url: HttpUrl
    name: str
    
    
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]
    
    
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None
    
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.get("/")
async def root():
    return {"message": "Hello there"}


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=6, max_length=50, regex="^fixedquery$")): 
    # in making the param required, you will use ellipses instead of None
    # http://localhost:8000/items/?q=foo&q=bar
    
    # q: Optional[str] = Query(
    #     None,
    #     alias="item-query",
    #     title="Query string",
    #     description="Query string for the items to search in the database that have a good match",
    #     min_length=3,
    #     max_length=50,
    #     regex="^fixedquery$",
    #     deprecated=True,
    # )
    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get", ge=1),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = Body(None, embed=True),
    user: User,
    importance: str = Body(..., title="The body importance")
):
    results = {"item_id": item_id, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


# Don't do this in production!
@app.post("/user/", response_model=UserOut, response_model_exclude_unset=True, response_model_exclude=["tax"])
async def create_user(user: UserIn):
    return user


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# partial updates to a model
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True) # the exclude_unset is required for a partial update
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item