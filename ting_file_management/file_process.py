from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_path = ""

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            file_path = instance.search(index)

    if file_path == "":
        file = txt_importer(path_file)
        lines = len(file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines,
            "linhas_do_arquivo": file,
        }
        instance.enqueue(result)
        print(f"{result}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
