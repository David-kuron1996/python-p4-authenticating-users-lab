#!/usr/bin/env python3

import pytest
from app import app, db
from models import User, Article

@pytest.fixture(autouse=True)
def setup_database():
    with app.app_context():
        db.create_all()
        
        # Clear existing data
        User.query.delete()
        Article.query.delete()
        
        # Create test users
        test_user = User(username='testuser')
        db.session.add(test_user)
        db.session.commit()
        
        yield
        
        # Cleanup after tests
        db.session.remove()
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))