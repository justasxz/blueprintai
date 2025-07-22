from flask import Blueprint, render_template
from classes.post import Post

blog_bp = Blueprint('blog', __name__, url_prefix='/', template_folder='../templates')

@blog_bp.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=posts)