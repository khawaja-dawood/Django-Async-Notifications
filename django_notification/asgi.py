"""
ASGI config for django_notification project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import notification.routing
from notification import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_notification.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    # 'websocket': URLRouter(routing.ws_patterns)
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            notification.routing.websocket_url_patterns
        )
    )
})