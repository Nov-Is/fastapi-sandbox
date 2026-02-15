from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

# パスパラメータの型が宣言できる
# バリデーションもできるらしい、素晴らしい
@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"item_id": item_id}

# おそらく具体的なパスを先に書けということかな、変数は後で書くべし
@app.get("/users/me")
async def read_user_me():
  return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
  return {"user_id: user_id"}

# 再定義不可
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# enumでの指定 import, class定義を忘れずに
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  # isはオブジェクトそのものかを判定
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}
  #  ==は値が同じか
  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}

  return {"model_name": model_name, "message": "Have some residuals"}

