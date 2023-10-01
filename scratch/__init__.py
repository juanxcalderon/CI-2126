import json
import os
import shlex
import itertools

import check50


@check50.check()
def valid():
    """El proyecto existe y es un programa Scratch válido"""

    # Make sure there is only one .sb3 file.
    filenames = [filename for filename in os.listdir() if filename.endswith(".sb3")]

    if len(filenames) > 1:
        raise check50.Failure("Se encontró más de un archivo .sb3. ¡Asegúrate de que haya solo uno!")
    elif not filenames:
        raise check50.Failure("no se encontró ningún archivo .sb3")

    filename = filenames[0]

    # Ensure that unzipped .sb2 file contains .json file.
    if check50.run(f"unzip {shlex.quote(filename)}").exit():
        raise check50.Failure("archivo .sb3 inválido")
    check50.exists("project.json")

    with open("project.json") as f:
        project = json.load(f)

    return project["targets"]

@check50.check(valid)
def two_sprites(project):
    """El proyecto contiene al menos dos sprites."""

    num_sprites = sum(not target["isStage"] for target in project)

    if num_sprites < 2:
        raise check50.Failure(f"solo {num_sprites} sprite{'' if num_sprites == 1 else 's'} encontrados, se requieren 2")

@check50.check(valid)
def non_cat(project):
    """el proyecto contiene un sprite que es no-cat"""

    cat_sprite_ids = {"bcf454acf82e4504149f7ffe07081dbc",
                      "0fb9be3e8397c983338cb71dc84d0b25"}

    if all(target["isStage"] or {costume["assetId"] for costume in target["costumes"]} == cat_sprite_ids for target in project):
        raise check50.Failure("ningún sprite non-cat encontrado")

@check50.check(valid)
def three_blocks(project):
    """el proyecto contiene al menos tres guiones"""

    num_blocks = sum(len(target["blocks"]) for target in project)
    if num_blocks < 3:
        raise check50.Failure(f"solo {num_blocks} script{'' if num_blocks == 1 else 's'} encontrados, se requieren 3")

@check50.check(valid)
def uses_condition(project):
    """el proyecto utiliza al menos un condicional"""

    if not contains_blocks(project, ["control_repeat", "control_if_else", "control_if", "motion_ifonedgebounce"]):
        raise check50.Failure("ningún condicional encontrado, se requiere 1")

@check50.check(valid)
def uses_loop(project):
    """el proyecto utiliza al menos un bucle"""

    # Search project scripts for a repeat, repeat until, or forever block.
    if not contains_blocks(project, ["control_forever", "control_repeat_until", "control_repeat"]):
        raise check50.Failure("ningún bucle encontrado, se requiere 1")

@check50.check(valid)
def uses_variable(project):
    """el proyecto utiliza al menos una variable"""

    if not any(target["variables"] for target in project):
        raise check50.Failure("ninguna variable encontrada, se requiere 1")

@check50.check(valid)
def uses_custom_block(project):
    """el proyecto utiliza al menos un bloque personalizado"""

    if "custom_block" not in json.dumps(project):
        raise check50.Failure("no se encontraron bloques personalizados, se requiere 1")

def contains_blocks(project, opcodes):
    """Devuelve si el proyecto contiene bloques con sus nombres en los códigos de operación"""
    return any(any((isinstance(block, dict) and block["opcode"] in opcodes) for block in target["blocks"].values())
               for target in project)
