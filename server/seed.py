#!/usr/bin/env python3

from app import app
from models import db, Article, User

with app.app_context():
    
    print("Creating tables...")
    db.create_all()

    print("Deleting all records...")
    Article.query.delete()
    User.query.delete()

    print("Creating users...")
    users = [
        User(username="testuser"),
        User(username="alice"),
        User(username="bob"),
    ]

    db.session.add_all(users)

    print("Creating articles...")
    articles = [
        Article(
            author="Test Author",
            title="Test Article 1",
            content="This is a test article content for testing purposes.",
            preview="This is a test...",
            minutes_to_read=5,
            user_id=1
        ),
        Article(
            author="Another Author",
            title="Test Article 2", 
            content="Another test article with different content for testing.",
            preview="Another test...",
            minutes_to_read=3,
            user_id=2
        ),
    ]

    db.session.add_all(articles)
    
    db.session.commit()
    print("Complete.")