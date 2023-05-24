from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjUyNDQyMTE4LCJpYXQiOjE2NTE4MzczMTgsInN1YiI6IjIifQ.5yeW2y_M3eAYrv-369FLsTTkjAFQn6W_eUR19Ivz_YA
Tipo: bearer

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjUyNDQzNDk1LCJpYXQiOjE2NTE4Mzg2OTUsInN1YiI6IjMifQ.jTq0xkcILa7kgrtMJhcew6OIwXODEjX24CzCToY7bbU

---

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjg1NTM3NDY0LCJpYXQiOjE2ODQ5MzI2NjQsInN1YiI6IjMifQ.NjhSzUyB_pCWNN3EVECMvmFBQq8KHFNFvWN0GcPpFCs"
Tipo: bearer



"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjg1NTM5NDM2LCJpYXQiOjE2ODQ5MzQ2MzYsInN1YiI6IjEifQ.9FfkDu38eLaKP9EfyrtOX9_1eUovHGdddGl4dDWWUrI",
  "token_type": "bearer"
"""


