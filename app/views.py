from flask import request, render_template, redirect, url_for,flash
from flask_login import login_user, logout_user, login_required
from app import db
from . import models
from . import forms


def transactions_list():
    transactions = models.Transactions.query.all()
    return render_template('transactions_list.html',transactions=transactions)

@login_required
def transactions_create():
    title = "Добавить транзакцию"
    save = 'Сохранить'
    form = forms.TransactionsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            transaction = models.Transactions()
            form.populate_obj(transaction)
            db.session.add(transaction)
            db.session.commit()
            flash('Транзакция прошла успешно!','success')
            return redirect(url_for('transactions_list'))
    return render_template('transactions_form.html',form=form,title=title,save=save)

def transactions_detail(id):
    tran = models.Transactions.query.get(id)
    return render_template('transactions_detail.html',tran=tran)

@login_required
def transactions_update(id):
    title = "Добавить транзакцию"
    save = 'Сохранить'
    student = models.Transactions.query.get(id)
    form = forms.TransactionsForm(request.form,obj=student)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transactions_form.html',form=form,title=title,save=save)

@login_required
def transactions_delete(id):
    tran = models.Transactions.query.get(id)
    if request.method == 'POST':
            db.session.delete(tran)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transactions_delete.html',tran=tran)

def register_view():
    title = 'Регистрация пользоваться'
    save = 'Зарегистрировать'
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = models.User()
            form.populate_obj(user)
            # user = models.User(username=request.form.get('username'))
            # user.set_password(request.form.get('password'))
            db.session.add(user)
            db.session.commit()
            flash(f'Пользователь {user.username} успешно зарегистрирован!','success')
            return redirect(url_for('login'))
    return render_template('transactions_form.html', form=form,title=title,save=save)


def login_view():
    title = 'Войти'
    save = 'Войти'
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # user = models.User()
            # form.populate_obj(user)
            user = models.User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Успешно авторизован!','primary')
                return redirect(url_for('transactions_list'))
            else:
                flash('Неправильно введенные логин или пароль!', 'danger')
    return render_template('transactions_form.html', form=form,title=title,save=save)


def logout_view():
    logout_user()
    return redirect(url_for('transactions_list'))