def render_template(template_name, context):
    with open(f"templates/{template_name}", "r") as f:
        content = f.read()
    for key, value in context.items():
        content = content.replace(f"{{{{ {key} }}}}", str(value))
    return content
