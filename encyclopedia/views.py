from django.shortcuts import render
import markdown
from django import forms
from .util import get_entry
import markdown
from . import util
import random


def index(request):
    entries = ["CSS","Django", "Git", "HTML", "Python"]
    search_entry = request.GET.get("q")
    if search_entry:
        content = get_entry(search_entry)
        if content:
            return render(request, "encyclopedia/entry.html",{"title": search_entry, "content": content})
        else:
            entry_match = [entry for entry in entries if search_entry.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {"search_entry": search_entry, "entry_match" : entry_match})
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    content = get_entry(entry_name)
    if content:
        html_content = markdown.markdown(content)
    else:
        return render(request, "encyclopedia/error.html", {"message": "Entry not found"})
    
    return render(request, "encyclopedia/entry.html", {
        "title": entry_name,
        "content":html_content

    })
    
    

def create_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            return render(request, "encyclopedia/create_entry.html", {
                "error": "An entry with that title already exists."
            })
        util.save_entry(title, content)

        entries = util.list_entries()
        return render(request, "encyclopedia/index.html", {
            "entries": entries,
        })
    return render(request, "encyclopedia/create_entry.html")

def edit_entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "Entry not found."})
    if request.method == "POST":
        updated_content = request.POST["content"]
        util.save_entry(title, updated_content)
        return render (request, "encyclopedia/entry.html", {
            "title": title,
            "content": updated_content
        })
    return render(request, "encyclopedia/edit_entry.html", {
         "title": title,
         "content": content
    })

def random_entry(request):
    entries = util.list_entries()
    if entries:
        random_title = random.choice(entries)
        return render(request, "encyclopedia/entry.html", {
            "title": random_title,
            "content": util.get_entry(random_title)
        })
    else:
        return render(request, "encylopedia/error.html", {"message":"No entries available"})
    

