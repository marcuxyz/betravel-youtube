from mvc_flask import Router

Router.get('/', 'home#index')
Router.get('/medias/<name>', 'medias#upload')
Router.all('posts', only='show new create')
Router.all('categories', only='new create')
