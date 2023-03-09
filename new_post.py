import click
import datetime
import pytz

_post = """
---
layout: post
title: {title}
date: {date} -0400
---

# {title}
<!-- Put stuff in here -->

<script src="https://utteranc.es/client.js"
        repo="Just-Jojo/Just-Jojo.github.io"
        issue-term="pathname"
        label="Comments"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
""".strip() 

@click.group()
def blog():
    """Manage blog posts from the command line"""
    pass

@blog.command()
@click.option(
    "--title",
)
def new(title: str):
    """Create a new blog post"""
    date = datetime.datetime.now()
    t = pytz.timezone("US/Eastern")
    date = t.localize(date)
    _h_m = lambda x: f"0{x}" if x < 10 else x
    first = f"{date.year}-{_h_m(date.month)}-{_h_m(date.day)}"
    act = f"{first} {date.hour}:{date.minute}:{_h_m(date.second)}"
    file_name = f"{first}-{title.lower().replace(' ', '-')}.md"
    with open(f"./_posts/{file_name}", "w") as fp:
        fp.write(_post.format(title=title, date=act))
    print("Done")

if __name__ == "__main__":
    blog()
