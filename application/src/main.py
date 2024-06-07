from fastapi import FastAPI

app = FastAPI()

characters = {
    'alphabet': ['a', 'b'],
    'number': ['1', '3'],
    'symbol': ['^', '#']
}

list = ["a", "b", "c", "d"]


#get Functions
@app.get("/get/{word}")
def print_hello(word):
    return {word}


@app.get('/get/char/{index}')
def disp_characters(index):
    return characters.get(index)


@app.get("/get/{first_name}/{last_name}/{age}")
def get_full_name_and_age(first_name: str, last_name: str, age: int):
    full_name = first_name.title() + " " + last_name.title()
    if not age >= 99:
        return full_name, age
    else:
        return full_name, "age is not correct"


#post function
@app.post("/post/{dto}")
async def create_post(dto):
    list.append(dto)
    return list


#put functions
@app.put("/put/{find}/{replace}")
async def put_post(find, replace):
    key = list.index(find)
    list.insert(key, replace)
    list.remove(find)
    return list


print(characters.values())
print(characters.keys())


#delete functions
@app.delete("/delete/{x}")
async def delete_post(x):
    list.remove(x)
    return list


print(list)
