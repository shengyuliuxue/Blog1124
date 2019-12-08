import click
from blog.fakedata import fake_post, fake_category, fake_links

@click.command()
@click.option('--postnum', type=int)
@click.option('--catnum', type=int)
@click.option('--linknum', type=int)
def init_db(postnum, catnum, linknum):
    fake_post(postnum)
    fake_category(catnum)
    fake_links(linknum)
    print("successed init the db!")






