from django_components import component


@component.register("hello_world")
class HelloWorld(component.Component):
    template_name = "hello_world.pug"
