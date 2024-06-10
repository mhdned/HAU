# Import libraries and dependencies
from fastapi import Request
from fastapi.templating import Jinja2Templates

# Pointed to templates
templates = Jinja2Templates(directory="templates")


# Class definitions
class JinjaTemplateEngine:

    def __init__(self) -> None:
        pass

    # Response jinja template method
    def response(self, request: Request, name: str, context: dict):
        """
        Response HTML template with jinja engine

        Parameters:
        request (Request): Passing request type from built-in fastapi modules.
        name (string): Path with name after inside jinja template folder.
        context (dict): Variables to bind in the template.

        Returns:
        HTML response: When the API path in Finnish shows the client jinja template.

        Raises:
        IDK: IDK everything may raises error

        Examples:
        Just try to see the main route API

        """
        return templates.TemplateResponse(request=request, name=name, context=context)


jinja = JinjaTemplateEngine()
