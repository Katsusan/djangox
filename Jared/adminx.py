import xadmin

from Jared.models import User,Comment,Article,Tag


xadmin.site.register(User)
xadmin.site.register(Article)
xadmin.site.register(Tag)
xadmin.site.register(Comment)