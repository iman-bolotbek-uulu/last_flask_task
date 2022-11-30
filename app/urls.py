from app import app
from . import views

app.add_url_rule('/', view_func=views.transactions_list,
                 endpoint='transactions_list')

app.add_url_rule('/transactions/create', view_func=views.transactions_create, methods=['GET', 'POST'],
                 endpoint='transactions_create')

app.add_url_rule('/register',view_func=views.register_view,methods=['GET','POST'],endpoint='register')
app.add_url_rule('/login',view_func=views.login_view,methods=['GET','POST'],endpoint='login')
app.add_url_rule('/logout',view_func=views.logout_view,endpoint='logout')

app.add_url_rule('/transactions/<int:id>', view_func=views.transactions_detail, methods=['GET', 'POST'],
                 endpoint='transactions_detail')
app.add_url_rule('/transactions/<int:id>/update', view_func=views.transactions_update, methods=['GET', 'POST'],
                 endpoint='transactions_update')
app.add_url_rule('/transactions/<int:id>/delete', view_func=views.transactions_delete, methods=['GET', 'POST'],
                 endpoint='transactions_delete')