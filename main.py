from fastapi import FastAPI
from routers import user, image, login, useraddress, category, product, feedback, wishlist, cart

app = FastAPI()

app.include_router(user.router)
app.include_router(image.router)
app.include_router(login.router)
app.include_router(useraddress.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(feedback.router)
app.include_router(wishlist.router)
app.include_router(cart.router)