from project import db
from project.models import User

# Inserto data
db.session.add(User("admin", "admin@admin.com", "admin"))
db.session.add(User("nltattessi", "nltattessi@gmail.com", "nahlatk2409"))

# Commiteo
db.session.commit()