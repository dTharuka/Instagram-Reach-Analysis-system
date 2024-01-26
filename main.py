import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = pd.read_csv("Instagram data.csv", encoding='latin1')
print(data.head())

data.isnull().sum()

data = data.dropna()

data.info()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")

# plt.show()


@app.get("/chartOne")
async def get_chart_one():
    # Create a chart and save it as a PNG image
    plt.figure(figsize=(8, 4))
    sns.distplot(data['From Home'])
    # Add your plotting logic here
    plt.title("Your Chart Title")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode()
    plt.close()
    return {"image_data": img_str}

@app.get("/chartTwo")
async def get_chart_two():
    # Create a chart and save it as a PNG image
    plt.figure(figsize=(8, 4))
    sns.distplot(data['From Hashtags'])
    # Add your plotting logic here
    plt.title("Distribution of Impressions From Hashtags")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode()
    plt.close()
    return {"image_data": img_str}


@app.get("/chartThree")
async def get_chart_three():
    # Create a chart and save it as a PNG image
    plt.figure(figsize=(8, 4))
    sns.distplot(data['From Explore'])
    # Add your plotting logic here
    plt.title("Distribution of Impressions From Explore")
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode()
    plt.close()
    return {"image_data": img_str}