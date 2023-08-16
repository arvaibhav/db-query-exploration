import django_setup
import django
from django.apps import apps
from django.db.models.deletion import (
    DO_NOTHING,
    CASCADE,
    PROTECT,
    SET_NULL,
    SET_DEFAULT,
)

django.setup()


def on_delete_action(field):
    actions = {
        DO_NOTHING: "DO NOTHING",
        CASCADE: "CASCADE",
        PROTECT: "PROTECT",
        SET_NULL: "SET NULL",
        SET_DEFAULT: "SET DEFAULT",
    }
    return actions.get(field.remote_field.on_delete, "")


def generate_markdown():
    models = apps.get_models()
    markdown_content = ""

    for model in models:
        table_name = model._meta.db_table
        markdown_content += f"## {model.__name__} (Table Name: {table_name})\n"
        markdown_content += "| Field Name | Type | Constraints | On Delete | Index |\n"
        markdown_content += "|------------|------|-------------|-----------|-------|\n"

        for field in model._meta.fields:
            field_name = field.name
            field_type = field.get_internal_type()

            constraints = []
            if field.primary_key:
                constraints.append("Primary Key")
            if field.unique:
                constraints.append("Unique")
            if not field.null:
                constraints.append("Not Null")
            if field.default != django.db.models.fields.NOT_PROVIDED:
                constraints.append(f"Default: {field.default}")

            on_delete = ""
            if field.remote_field and field.remote_field.on_delete:
                on_delete = on_delete_action(field)

            index = "Yes" if field.db_index else "No"

            markdown_content += f'| {field_name} | {field_type} | {", ".join(constraints)} | {on_delete} | {index} |\n'

        for constraint in model._meta.constraints:
            markdown_content += (
                f"| Constraint: {constraint.name} | - | {str(constraint)} | - | - |\n"
            )

        markdown_content += "\n\n"

    return markdown_content


if __name__ == "__main__":
    markdown_schema = generate_markdown()
    with open("../sql_schema.md", "w") as file:
        file.write(markdown_schema)
    print("Markdown schema has been written to sql_schema.md")
