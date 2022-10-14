from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import APIKeyHeader
import os
import uvicorn
from pydantic import BaseModel
import pickle


# Load model -----------------------------------------------------------------------------------------------------------
with open('./src/model.pickle', 'rb') as f:
    MODEL = pickle.load(f)


# Define ApiKey settings -----------------------------------------------------------------------------------------------
X_API_KEY = APIKeyHeader(name='X-API-Key')


def api_key_auth(x_api_key: str = Depends(X_API_KEY)):
    """
    Takes the X-API-Key header and validate it with the X-API-Key in the environment variable "API_KEY"
    """
    if x_api_key != os.environ.get('API_KEY'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key. Check that you are passing a 'X-API-Key' on your header.",
            headers={"Authorization": "X-API-Key"}
        )


# Define response Models and Exceptions -------------------------------------------------------------------------------
class Iris(BaseModel):
    label_predicted: str

    class Config:
        schema_extra = {
            "example": {
                "label_predicted": "setosa"
            }
        }


# Start FastAPI app ----------------------------------------------------------------------------------------------------
app = FastAPI()


@app.get("/")
async def home():
    return {"message": "API demo del Human Datathon 2022 está OK. Ir a '/docs' para acceder a la documentación."}


@app.get("/predict_plant",
         dependencies=[Depends(api_key_auth)],
         response_model=Iris
         )
async def predict_plant(sepal_lenght: float, sepal_width: float, petal_lenght: float, petal_width: float) -> dict:
    """
    Predict type of plant. <br>
    :param sepal_lenght: float - sepal length (cm) <br>
    :param sepal_width: float - sepal width (cm) <br>
    :param petal_lenght: float - petal length (cm) <br>
    :param petal_width: float -  petal width (cm) <br>
    :return: str - ["setosa", "versicolor", "virginica"]
    """

    return {'label_predicted': MODEL.predict([[sepal_lenght, sepal_width, petal_lenght, petal_width]])[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, debug=True)
