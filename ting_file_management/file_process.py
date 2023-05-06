from ting_file_management.file_management import txt_importer
import sys


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
    if not len(instance):
        return print("Não há elementos")
    first_item = instance.dequeue()
    print(f"Arquivo {first_item['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(f"{instance.search(position)}")
    except IndexError:
        print("Posição inválida", file=sys.stderr)
