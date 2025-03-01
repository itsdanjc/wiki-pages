# WikiPages

WikiPages is being built for the ["pages"](https://itsdanjc.com/pages/) part of my site – a mashup of a blog and a wiki. It’s designed to be lightweight, fast, 
and dead simple to use.

Whether you want to document a project, build a knowledge base, or just have a place to dump notes, WikiPages has you covered. 
And the best part? It’s flexible. You can slap it onto any site and turn it into your own wiki with minimal setup. No bloated features, no overcomplication - just 
a clean, Git-powered way to manage your content.

## Table Of Contents
- [Introduction](#wikipages)
- [Features](#features)
- [Installation](#installation)
  - [Automatic](#automatic-installation-recommended)
  - [Manual](#manual-installation)
- [Contribute](#contribute)


## Features
> [!NOTE]
> The project is very much still in development. Most of the features are 
> not implemented yet.

- **Git-Powered:** Built on Git, a powerful version control system.
- **Content Organization:** Group your pages with categories. Cover multiple topics? Create mini sub-wikis to keep things tidy.
- **Easy Editing:** Enjoy quick, hassle-free editing with Markdown and syntax highlighting.
- **Admin Dashboard:** Rollback changes, lock pages, manage permissions, and manage your wiki easily with the admin tools.
- **CLI** - Manage the workings of WikiPages seamlessly.
- **API** - The built in APIs allow WikiPages to work with your apps and services.
- **SEO-Ready:** WikiPages is optimized for search engines right out of the box. Just set it up and you're good to go.
- **Templated Design** - Pages are created from structured templates, allowing pages to look great on all devices. Need further customization? Create your own templates easily.
- **Content Management** - Users can add images videos and even files to pages. WikiPages can integrate storage provides like AWS, Google Cloud or Azure.
- **Server Rendering** - Markdown gets converted to HTML only when a page changes. That means no extra processing on every load, which boosts performance for both the client and server.
- **Seamless Integration:** Let users log in with OAuth services like GitHub, GitLab, Azure, and more - perfect for a documentation platform.
- **Flexible Setup** Configure each part of WikiPages independently, from a minimal install to a high-availability setup - and everything in between.

**Got feature suggestions?** Got any ideas to make WikiPages even better? Drop your thoughts by opening a feature suggestion on GitHub!

**Want to contribute?** - Jump in and help the development of WikiPages - [read how](#contribute) below!

## Installation
### Automatic installation (Recommended)
1. #### Download and run `install.py`

    ```bash
    curl -O https://raw.githubusercontent.com/itsdanjc/wiki-pages/refs/heads/development/install.py && python install.py
    ```
    This command pulls down the installer, clones the repo, sets things up, and installs all the dependencies for WikiPages.

2. #### Start WikiPages:
    
    ```bash
    python app.py
    ```
    If you’ve enabled debug mode, your terminal should show something like this:

    ```bash
    [API] INFO: API module configured
    [UI] INFO: UI module configured
    [API] INFO: Log at /var/log/wikipages/wikipages_api_2025-03-01.tmp.log
    [UI] INFO: Log at /var/log/wikipages/wikipages_ui_2025-03-01.tmp.log
    ```

    And that’s it - WikiPages is up and running!

### Manual installation
If you prefer to do it step-by-step (or have special requirements), follow these:

1. #### Clone the repo

    ```bash
    git clone https://github.com/itsdanjc/wiki-pages.git
    cd wiki-pages
    ```

2. #### Install dependencies

    ```bash
    python -m venv .venv
    pip install -r requirements.txt
    ```

3. #### <s>Create new git repo for article storage</s>
  > [!NOTE]
  > This step isn’t implemented yet - skip it for now.

4. #### Create a configuration file

    **Linux:**
    ```bash
    sudo nano /etc/wikipages/wikipages.conf
    ```

    **Windows / macOS:**
    ```bash
    ./wikipages.conf
    ```

5. #### Start WikiPages:
    
    ```bash
    python app.py
    ```
    If you're in debug mode, you should see output like:

    ```bash
    [API] INFO: API module configured
    [UI] INFO: UI module configured
    [API] INFO: Log at /var/log/wikipages/wikipages_api_2025-03-01.tmp.log
    [UI] INFO: Log at /var/log/wikipages/wikipages_ui_2025-03-01.tmp.log
    ```

    Now you're all set - WikiPages is fully installed and ready to rock!

## Using the CLI
> [!NOTE]
> The project is very much still in development. The CLI is included as feature not currently avaliable.

## Contribute

First off, thanks for wanting to contribute! Whether it’s fixing a bug, adding a feature, or just sharing ideas, all contributions are welcome.

### Got a feature idea?  
If you’ve got a cool idea that could make WikiPages better, open a [feature suggestion](https://github.com/itsdanjc/wiki-pages/issue?category=suggestion) on GitHub.

### Found a bug?  
It would really help the development by opening an [issue](https://github.com/itsdanjc/wiki-pages/issues?category=issues). Try to include as much detail as possible (logs, steps to reproduce, etc.) to make it easier to fix.

### Want to contribute code?  
Check out the WikiPages' [wiki](https://github.com/itsdanjc/wiki-pages/wiki) for reference documentation.
